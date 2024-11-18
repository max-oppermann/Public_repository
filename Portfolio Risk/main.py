import sys
import numpy as np

import datafetch as df

def main():
    """TO DO:
    get list of stocks
    get list of weights for those stocks
    get target/risk free rate
    
    process_data to get individual returns
    portfolio_returns + weights from above for portfolio returns
    
    risk_contributions from individual returns + weights
    
    VaR/CVaR/ for those historical portfolio returns
    Sharpe/Sortino for that portfolio
    drawdowns and cumulative get calculated in their plotting functions
    plot_var_cvar() takes returns
    
    simulated returns for plotting + their VaR/CVaR
    but monte_carlo_var takes the simple 'returns' as argument
    
    6 plotting functions
    """

def get_stocks() -> list:
    """Prompts the user to input stock tickers or retrieves them from command line.
    
    If tickers are present in the CL, they are returned as a list. 
    If no command-line tickers are given, the function prompts the user to input tickers one by one. 
    The user can type 'done' to finish the input. These ticker inputs are verified, but not 
    the tickers from the command line (presumably you want to be fast then).

    Returns:
        list: A list of stock ticker symbols (strings).
    """
    
    # using command line, the symbols just need to be correct
    if len(sys.argv) > 1:
        return sys.argv[1:]
   
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
    """Prompts the user to input the target rate manually. Intended for Sharpe/Sortino ratio.
    
    Returns:
        float: The target rate as a decimal (e.g., 0.03 for 3%).
    """
    while True:
        try:
            rate = float(input("Enter the current (daily) target rate (as a percentage, e.g., 0.001 for 0.001%): "))
            return rate / 100  # percentage to decimal
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            

def get_weights(stock_symbols: list) -> np.ndarray:
    """Prompts the user for which weights should be assigned.

    If custom weights are selected, the function ensures they sum to 1. If no custom weights 
    are provided, the user can pick between equal or market cap weights. The return values are 
    as they are because of how the function portfolio_returns() in  works datafetch.py
    
    Args:
        stock_symbols (list): List of stock tickers for which weights will be assigned.

    Returns:
        np.ndarray: Array of portfolio weights. Or string 'equalweights', or 'None'.
    """
    while True:
        reply = input("Do you have custom weights (y/n)? ").strip().lower()
        if reply[0] in ['y', 'n']:
            break
        print("Illegitimate input")

    if reply[0] == 'y':
        total_weight = 0
        weights = np.zeros(len(stock_symbols))
        for i, stock in enumerate(stock_symbols):
            weight = float(input(f"Weight for {stock}: "))
            total_weight += weight
            if total_weight < 1 and i == len(stock_symbols) - 1:
                weights[i] = weight
                print("Final stock reached, but total weight != 1. Increasing all weights.")
                return weights / total_weight
            if total_weight < 1:
                weights[i] = weight
                continue
            if total_weight == 1 and i < len(stock_symbols) - 1:
                weights[i] = weight
                print("Total weight of 1 reached. Assigning weight 0 to the rest.")
                break
            if total_weight > 1:
                weights[i] = 1 - (total_weight - weight)
                print("Total weight is larger than 1. Truncating weights.")
                return weights / total_weight
        return weights
    
    specification = input("Market capitalization weights or 'equalweights'?")
    if specification.strip().lower() == 'equalweights':
        return 'equalweights'
    return None


if __name__ == "__main__":
    main()