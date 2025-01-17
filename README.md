If you're a potential employer, you may be interested in my [Big Five traits](cognitive-metrics/Big-Five/README.md). If you are interested in my *g*eneral cognitive ability, [this](cognitive-metrics/README-g.md) may be interesting. I can also predict [my percentile rank](cognitive-metrics/README-quant.md) in job performance directly (with some error, 99.5th percentile in high complexity jobs, somewhat lower in lower complexity jobs).

Roughly in order of importance and recency:

# Portfolio Risk  

Contains a Python project for analyzing stock portfolios using historical data, risk metrics, and future return simulations. The analysis outputs a visual dashboard summarizing portfolio performance and risk.  
Modularly designed with components for data fetching, risk calculations (e.g., VaR), future simulations, and visualization. For detailed information on usage, features, and examples, see the project README.

# Probability Simulations

Programs of varying length and complexity with the theme of probability theory. `gamblers_ruin.py` is currently the nicest program.  

`gamblers_ruin.py` simulates and plots variations of Gambler's ruin as a Markov chain.  
`ht_before_hh.py` tossing a fair coin, HH on average occurs later than HT.  
`matching_cards.py` simulates matching cards problem with 100 cards.  
`metropolis_hastings_normal.py` demonstrates the Normal–Normal conjugacy via MCMC using Metropolis-Hastings.  
`monty_hall.py` let's you play the classic Monty Hall set up.  
`uniform_universality.py` demonstrates the 'universality of the Uniform.'  
`pi_estimate_mc.py` Monte Carlo integration to estimate the value of $\pi$ (very short).  
`poisson_process.py` simulates and plots a Poisson process.  
`winners_curse.py` shows expected payoff for bidding on a mystery prize with variable thresholds for when the bid is accepted. Don't play for threshold $\gt 0.5$.

# Wahldaten-Analyse

Dieser Ordern enthält ein Notebook, das eine kleine Beispielanalyse der Wahlergebnisse im Lande Bremen der Bundestagswahl 2021 auf Stadtteilebene beschreibt. Es geht mir v. a. darum, eine breite Palette an statistischem Wissen zu demonstrieren; die tatsächlichen Ergebnisse der Analyse sind nachrangig. Man kann sich das hier in GitHub angucken, aber die Hyperlinks vom und zum Inhaltsverzeichnis funktionieren dann nicht. Man klicke stattdessen [hier](https://nbviewer.org/github/max-oppermann/Public_repository/blob/master/Wahldaten-Analyse/Wahldaten_Analyse.ipynb) oder, wenn das nicht funktioniert, gehe zu https://nbviewer.org/ und füge den Link zum Notebook in meinem Repository ein (dieser hier: https://github.com/max-oppermann/Public_repository/blob/master/Wahldaten-Analyse/Wahldaten_Analyse.ipynb).

This directory contains a  notebook (exclusively in German!) with an example analysis of the 2021 federal election results in Germany's federal state of Bremen using county-level data. It's mostly about showcasing a broad range of statistical knowledge; the actual results of the analysis are secondary.

# Anki Decks  

Some flashcard decks for the flashcard learning app Anki. The field "Source" will usually give the source as "author, *title of the book*, [number of chapter] (title of the chapter)". For example: "Hastie; Tibshirani, *Introduction to Statistical Learning*, 3 (Linear Regression)". Sometimes there are additions like "Lab" for the labs in ISLP or "Ex. [number]" for the exercises in Blitzstein.  
- *Blitzstein, Probability*. Enormous! Around 1400 notes and 1600 cards. The entire textbook "Introduction to Probability" by Blitzstein and Hwang; i. e., practically all theorems and definitions, almost all proofs for those theorems, almost all examples, the large majority of exercises and solutions. I left out exercises that only seemed like tedious calculations or were repeating a concept already covered sufficiently (in my estimation).  
- *ISLP*. Around 600 cards and notes. The video lectures, book chapters, labs, and some bits from the programming exercises from "An Introduction to Statistical Learning with Applications in Python" by Hastie, Tibshirani et al.  
- *Freedman, Statistical Models*. Around 250 notes and 350 cards. A more superficial treatment of "Statistical Models" by David Freedman (not to be confused with "Statistics" by Freedman, Purves, and Pisani). Exercises only if solutions were available.

# Exercises for ISLP

What it says on the tin; the programming exercises from the book "An Introduction to Statistical Learning with Applications in Python" by Hastie, Tibshirani et al. For more, see the notebook (the free floating file `Exercises-ISLP.ipynb`). The table of contents isn’t functional on GitHub; click [here](https://nbviewer.org/github/max-oppermann/Public_repository/blob/master/Exercises-ISLP.ipynb) instead. If that does not work, use https://nbviewer.org/ and paste the link to the notebook within my repository, i. e., https://github.com/max-oppermann/Public_repository/blob/master/Exercises-ISLP.ipynb, to have a functional  ToC.

# Algorithms I

Weeks 1–5 of the Coursera Course “Algorithms, Part I” by Robert Sedgewick entail exercises necessary to pass the course (at least 80% per exercise according to the autograder). Getting a certificate for passing the course costs money, so this is my proof I finished the course. The entire course is in Java, which I had never used before and would like to never use again (except for Part II, maybe). Luckily it is relatively similar to C, in my opinion.  
Week 1: Percolation. 100%. [specification](https://coursera.cs.princeton.edu/algs4/assignments/percolation/specification.php)  
Week 2: Deques and Randomized Queues. 98%. [specification](https://coursera.cs.princeton.edu/algs4/assignments/queues/specification.php)  
Week 3: Collinear Points. 95% (pretty hard!). [specification](https://coursera.cs.princeton.edu/algs4/assignments/collinear/specification.php)  
Week 4: 8 Puzzle. 97%. [specification](https://coursera.cs.princeton.edu/algs4/assignments/8puzzle/specification.php)   
Week 5: Kd-Trees. 85% (one of the functions does not actually solve the problem, but only gets very close). [specification](https://coursera.cs.princeton.edu/algs4/assignments/kdtree/specification.php)  

The “specifications” are the actual exercises and give an idea of the (considerable) complexity of these problems.

# CS50

CS50P is relatively unremarkable. The exercises can be found on the courses [website](https://cs50.harvard.edu/python/2022/) on the left within each week’s material.  

I did the 2024 version of [CS50x](https://cs50.harvard.edu/x/2024/). There are some interesting exercises: “tideman” in Pset3, all of Pset5, “fiftyville” in Pset7, and “finance” in Pset9:  
Tideman and Inheritance (Pset5) use recursive functions, making them substantially more complicated than the other exercises. Fiftyville is simply fun – although I probably didn’t do it as intended since I manually inferred the correct answer via several separate SQL queries.  
Finance is about creating a website where users can trade stocks with fictitious money and where all trades can be accessed in a history; the prices are actually real time prices for the stocks via requests from the web. It isn’t particularly complicated, but combines lots of Python code to interact with a server (via Flask) and a database and html templates. Lots of the code is actually written for you, which poses its own challenges of understanding ca. 100 lines of someone else’s code. On the other hand, it’s necessary to modify the database, work that is not apparent just from looking at it. For a detailed view of how much work is done by the student it’s probably easier to look at the original exercise and compare to my code.
