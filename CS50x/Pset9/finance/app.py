import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# (printing values as {{ value | usd }} instead of {{ value }}.
@app.route("/")
@login_required
def index():
    user = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
    user_cash = user[0]['cash']
    portfolio = db.execute("SELECT * FROM portfolio WHERE user_id = ?", session["user_id"])
    stock_total = 0
    stocks = []
    for p in portfolio:
        try:
            current_price = lookup(p['symbol'])['price']
        except:
            current_price = 0
            pass
        stocks.append({'symbol': p['symbol'], 'shares': p['shares'], 'c_p': usd(
            current_price), 'total': usd(current_price * p['shares'])})
        stock_total += (current_price * p['shares'])

    cash_balance = usd(float(user_cash))
    grand_total = usd(stock_total + float(user_cash))

    return render_template("index.html", user=user, portfolio=stocks, stock_total=stock_total, cash_balance=cash_balance, grand_total=grand_total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "POST":
        symbol = request.form.get("symbol")
        num_shares = request.form.get("shares")

        if not symbol:
            return apology("Missing stock symbol")

        stock = lookup(symbol)
        if stock == None:
            return apology("Symbol does not exist")
        try:
            num_shares = int(num_shares)
        except:
            return apology("Not an integer")
        if num_shares < 1:
            return apology("You need to buy at least one share")

        price = (stock['price'] * num_shares)
        money = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        user_money = money[0]['cash']

        if price > user_money:
            return apology("You do not have enough money in your account for this purchase")

        db.execute("INSERT INTO purchases (user_id, symbol, shares, price) VALUES(?, ?, ?, ?)",
                   session["user_id"], symbol, num_shares, stock['price'])

        if not db.execute("SELECT * FROM portfolio WHERE user_id = ? AND symbol = ?", session["user_id"], symbol):
            db.execute("INSERT INTO portfolio (user_id, symbol, shares) VALUES(?, ?, ?)", session["user_id"], symbol, num_shares)
        else:
            db.execute("UPDATE portfolio SET shares = shares + ? WHERE user_id = ? AND symbol = ?",
                       num_shares, session["user_id"], symbol)

        db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", price, session["user_id"])

        return redirect("/")

    else:
        return render_template("buy.html")

#(printing values as {{ value | usd }} instead of {{ value }}.
@app.route("/history")
@login_required
def history():
    purchases = db.execute("SELECT * FROM purchases WHERE user_id = ?", session["user_id"])
    sales = db.execute("SELECT * FROM sales WHERE user_id = ?", session["user_id"])
    if not sales and not purchases:
        return apology("No transactions found")
    for p in purchases:
        p['price'] = usd(p['price'])

    for s in sales:
        s['price'] = usd(s['price'])

    return render_template("history.html", purchases=purchases, sales=sales)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method == "POST":
        symbol = request.form.get("symbol")
        stock = lookup(symbol)
        if not symbol:
            return apology("Missing stock symbol")
        if stock == None:
            return apology("Symbol does not exist")

        stock["price"] = usd(stock["price"])

        return render_template("quoted.html", stock=stock)

    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        user_exists = db.execute("SELECT username FROM users WHERE username = :username", username=username)
        if user_exists:
            return apology("Username already exists")

        if not username or not password or not confirmation:
            return apology("Missing input")
        if password != confirmation:
            return apology("Passwords do not match")
        if not any(c.isdigit() for c in password):  # AI-duck version; much more concise
            return apology("Passwords needs to contain at least one number 0–9")

        hash = generate_password_hash(password)
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, hash)
        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    if request.method == "POST":
        shares = request.form.get("shares")
        symbol = request.form.get("symbol")
        owned_shares = db.execute("SELECT shares FROM portfolio WHERE user_id = ?", session["user_id"])

        if not symbol:
            return apology("Please select a stock to sell")
        try:
            shares = int(shares)
        except:
            return apology("Not an integer")
        if owned_shares == [] or shares > owned_shares[0]['shares']:  # order important to avoid IndexError
            return apology("You do not own that many shares")
        if shares < 1:
            return apology("You need to sell at least one share")
        sell_value = shares * lookup(symbol)['price']
        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", sell_value, session["user_id"])
        db.execute("UPDATE portfolio SET shares = shares - ? WHERE user_id = ? AND symbol = ?", shares, session["user_id"], symbol)

        db.execute("INSERT INTO sales (user_id, symbol, shares, price) VALUES(?, ?, ?, ?)",
                   session["user_id"], symbol, shares, lookup(symbol)['price'])
        return redirect("/")

    else:
        symbols = db.execute("SELECT symbol FROM portfolio WHERE user_id = ?", session["user_id"])
        return render_template("sell.html", symbols=symbols)
