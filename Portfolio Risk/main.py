"""
This module provides a comprehensive workflow for portfolio analysis, integrating data retrieval,
risk metrics calculation, and visualization. It allows users to analyze historical and simulated
performance of a portfolio, compute various financial metrics, and visualize results.

Faster to run from the command line. Accepts start and end dates for the portfolio analysis
and a list of stock ticker symbols. The weights and target rate (e.g., risk-free rate) are
supplied via user input.

Key Features:
- Retrieves historical stock price data for a specified portfolio.
- Computes portfolio metrics, including returns, risk contributions, Sharpe and Sortino ratio.
- Simulates future portfolio returns.
- Visualizes results via a dashboard with multiple plots, including cumulative returns,
  drawdowns, and Value at Risk (VaR) metrics.

Example:
    python main.py --start 2023-01-01 --end 2023-12-31 AAPL MSFT GOOGL
"""

import argparse
from datetime import datetime
import tkinter as tk

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import datafetch as df
import future_simulation as fs
import risk_metrics as rm
import visualization as vis

CONFIDENCE_LEVEL = 0.95 # for C/VaR calculations
METHOD = 'historical' # method vor VaR calculation, 'parametric' is the other option

NUM_SIM = 10000 # number of simulations when generating future returns
NUM_DAYS = 252 # for simulating future returns

LOWER_PCT = 5 # percentiles for CI in projecting cumulative returns; do not need to add to 1
UPPER_PCT = 95

YEAR_DAYS = 252 # for converting from annual to daily rate

def main(tickers: list, start_date: str, end_date: str):
    """Executes the main workflow for portfolio analysis.

    Args:
        tickers (list[str]): A list of stock ticker symbols for the portfolio.
        start_date (str): The start date for the portfolio's historical data.
        end_date (str): The end date for the portfolio's historical data.

    Workflow:
        1. Prompts the user to provide weights for the portfolio or assigns them automatically.
        2. Retrieves the target rate (daily or annual) for Sharpe and Sortino ratio calculations.
        3. Processes historical data for the specified tickers within the date range.
        4. Calculates portfolio returns and individual stock contributions to risk.
        5. Computes Sharpe and Sortino ratios based on the target rate.
        6. Generates a comprehensive dashboard with all calculated metrics and visualizations.
    """
    individual_returns = df.process_data(tickers=tickers, start_date=start_date, end_date=end_date)
    
    weights = get_weights(tickers=tickers)
    returns = df.portfolio_returns(tickers=tickers, start_date=start_date, end_date=end_date, weights=weights)

    target_rate = get_target_rate()
    risk_contributions = rm.risk_contributions(individual_returns=individual_returns, weights=weights)
    sharpe_ratio = rm.sharpe_ratio(returns=returns, target_rate=target_rate)
    sortino_ratio = rm.sortino_ratio(returns=returns, target_rate=target_rate)
    
    generate_dashboard(returns=returns,
                       risk_contributions=risk_contributions,
                       sharpe_ratio=sharpe_ratio,
                       sortino_ratio=sortino_ratio,
                       target_rate=target_rate)
    

def generate_dashboard(returns: pd.Series, risk_contributions: pd.DataFrame, sharpe_ratio: float, sortino_ratio: float, target_rate: float):
    """
    Generates a dashboard for portfolio analysis, dynamically adjusting the size to fit the screen.

    Args:
        returns (pd.Series): Portfolio returns over time.
        risk_contributions (pd.DataFrame): DataFrame with risk contributions per asset.
        sharpe_ratio (float): The portfolio's Sharpe ratio.
        sortino_ratio (float): The portfolio's Sortino ratio.
        target_rate: (float): The target rate; e.g. the risk-free rate.
    """
    # limiting the window size
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    screen_width_in = screen_width / 96
    screen_height_in = screen_height / 96
    
    scaling_factor = 0.9
    fig_width = min(screen_width_in * scaling_factor, 20)
    fig_height = min(screen_height_in * scaling_factor, 30)
    
    _, axs = plt.subplots(4, 2, figsize=(fig_width, fig_height))
    
    # plotting
    vis.pie_risk_contributions(risk_contributions["Normalized contribution"], axs[0, 0])
    axs[0, 0].set_title("Risk Contributions by Asset")
    
    axs[0, 1].axis("off")  # blanking the outer rectangle
    sharpe_sortino_text = f"Sharpe Ratio: {sharpe_ratio:.2f}\nSortino Ratio: {sortino_ratio:.2f}\
        \nTarget rate daily: {target_rate:.4%}\nTarget rate annual: {(1+target_rate)**252 - 1:.2%}"
    axs[0, 1].text(
        0, 0.75, # text in upper left corner
        sharpe_sortino_text,
        fontsize=16, fontweight="bold")
    
    vis.plot_historical_returns(returns, axes=axs[1, 0])
    vis.plot_cumulative_returns(returns, axes=axs[1, 1])
    vis.plot_drawdowns(returns, axes=axs[2, 0])
    
    var = rm.value_at_risk(returns, confidence_level=CONFIDENCE_LEVEL, method=METHOD)
    cvar = rm.conditional_value_at_risk(returns, confidence_level=CONFIDENCE_LEVEL)
    vis.plot_var_cvar(returns, var, cvar, axes=axs[2, 1])
    
    metrics = fs.monte_carlo_var(returns, num_sim=NUM_SIM, num_days=NUM_DAYS, confidence_level=CONFIDENCE_LEVEL)
    projection = fs.simulate_future_returns(returns, num_sim=NUM_SIM, num_days=NUM_DAYS)
    vis.plot_simulations(projection, metrics['daily']['VaR'], metrics['daily']['CVaR'],
                         num_paths=3, axes=axs[3, 0])
    vis.plot_simulations_cumulative(projection, metrics['cumulative']['CVaR'],
                                    lower_pct=LOWER_PCT, upper_pct=UPPER_PCT, axes=axs[3, 1])
    
    plt.tight_layout(rect=[0, 0.05, 1, 1])  # ensures no overlap
    plt.show()

def get_tickers(args) -> list:
    """Prompts the user to input stock tickers or retrieves them from command line.
    
    If tickers are present in the CL, they are returned as a list. 
    If no command-line tickers are given, the function prompts the user to input tickers one by one. 
    The user can type 'done' to finish the input. These ticker inputs are verified, but not 
    the tickers from the command line (presumably you want to be fast then).
    
    Args:
        args: The parsed command-line arguments.

    Returns:
        list: A list of stock ticker symbols (strings).
    """
    
    if args.tickers:
        return args.tickers
   
    tickers = []
    while True:
        ticker = input("Enter a stock ticker (or type 'done' to finish): ").strip().upper()
        if ticker.lower() == 'done':
            break
        if df.is_valid_ticker(ticker):
            tickers.append(ticker)
        else:
            print("Please enter a valid ticker symbol.")
    return tickers


def get_target_rate() -> float:
    """Prompts user for a daily or annual rate (converts latter to daily).

    Returns:
        float: The daily rate as a decimal.
    """
    while True:
        try:
            # Prompt the user for input
            rate_input = input(
                "Enter the target rate as a percentage (0.1 for 0.1%) for Sharpe/Sortino calculations:\n"
                "Use keywords 'yearly' or 'annually' after the rate if it's not a daily rate: "
            ).split()
            
            rate = float(rate_input[0]) / 100  # percentage to decimal
            
            if len(rate_input) == 1:
                return rate
            
            if rate_input[1].lower() in ['yearly', 'annually']:
                return (1 + rate) ** (1 / YEAR_DAYS) - 1  # annual to daily
            
            print("Invalid keyword. Use 'yearly' or 'annually' for annual rates.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid rate, optionally followed by 'yearly' or 'annually'.")


def get_weights(tickers: list) -> np.ndarray:
    """Prompts the user for which weights should be assigned.

    If custom weights are selected, the function ensures they sum to 1. If no custom weights 
    are provided, the user can pick between equal or market cap weights.
    
    Args:
        stock_symbols (list): List of stock tickers for which weights will be assigned.

    Returns:
        np.ndarray: Array of portfolio weights.
    """
    while True:
        reply = input("Do you have custom weights (y/n)? ").strip().lower()
        if reply[0] in ['y', 'n']:
            break
        print("Illegitimate input")

    # inputting custom weights, making sure they sum to 1
    if reply[0] == 'y':
        total_weight = 0
        weights = np.zeros(len(tickers))
        for i, stock in enumerate(tickers):
            while True:
                try:
                    weight = float(input(f"Weight for {stock}: ").strip())
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            total_weight += weight
            weights[i] = weight
            if total_weight < 1 and i == len(tickers) - 1:
                print("Final stock reached, but total weight != 1. Increasing all weights.")
                return weights / total_weight
            if total_weight < 1: # the normal inputting
                continue
            if total_weight == 1 and i < len(tickers) - 1:
                print("Total weight of 1 reached. Assigning weight 0 to the rest.")
                return weights
            if total_weight == 1 and i == len(tickers) - 1: # end of normal inputting
                return weights
            if total_weight > 1:
                print("Total weight is larger than 1. Truncating weights.")
                return weights / total_weight
    # equal or market cap weights
    specification = input("Market capitalization weights or 'equalweights'? ")
    if specification.strip().lower() == 'equalweights':
        weights = np.array([1 / len(tickers)] * len(tickers))
    else:
        weights = np.array(list(df.market_cap_weights(tickers).values()))

    return weights


def get_dates(args) -> tuple[str, str]:
    """Retrieves start and end dates for portfolio analysis.

    Args:
        args: The parsed command-line arguments (argparse.Namespace).

    Returns:
        tuple[str, str]: A tuple containing the start and end dates as strings.
    """
    # Use provided arguments or prompt the user
    start_date = args.start
    end_date = args.end
    
    if start_date is None or end_date is None:
        print("Missing date arguments. Please input values manually.")
        while not start_date:
            start_date = input("Enter the start date for portfolio history (YYYY-MM-DD): ").strip()
            if not is_valid_date(start_date):
                print("Invalid date format. Please enter a date in YYYY-MM-DD format.")
                start_date = None  # reset to keep loop going
        while not end_date:
            end_date = input("Enter the end date for portfolio history (YYYY-MM-DD): ").strip()
            if not is_valid_date(end_date):
                print("Invalid date format. Please enter a date in YYYY-MM-DD format.")
                end_date = None
    
    return start_date, end_date


def is_valid_date(date_str: str) -> bool:
    """Checks if a given string is a valid date in YYYY-MM-DD format."""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Retrieve start/end dates for portfolio analysis.")
    parser.add_argument('--start', type=str, help='Start date in YYYY-MM-DD format')
    parser.add_argument('--end', type=str, help='End date in YYYY-MM-DD format')
    parser.add_argument('tickers', nargs='*', help="List of stock ticker symbols to analyze.")
        
    arguments = parser.parse_args()
    START_DATE, END_DATE = get_dates(arguments)
    TICKERS = get_tickers(arguments)
    
    main(TICKERS, START_DATE, END_DATE)