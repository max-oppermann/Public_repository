import sys
import numpy as np
import matplotlib.pyplot as plt

import datafetch as df
import future_simulation as fs
import risk_metrics as rm
import visualization as vis

def main():
    """TO DO:
    get list of stocks
    get list of weights for those stocks
    get target/risk free rate
    'get' start and end dates
    
    process_data to get individual returns
    portfolio_returns + weights from above for portfolio returns
    risk_contributions from individual returns + weights
    Sharpe and Sortino ratio (requiring returns + target rate)

    generate_dashboard takes the simple portoflio returns, the DataFrame
    from risk_contributions, and the Sharpe/Sortino ratio
    
    6 plotting functions inside
    + the pie chart + Sharpe/Sortino
    
    --- go through all parameters again!!
        make them global variables in main.py:
        
    --- Also: modify get_target_rate to extrapolate from annual rate
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


def get_dates():
    """TO DO
    use argparse instead; gotta adjust get_stocks then. 
    See also gamblers_ruin.py
    
    parser = argparse.ArgumentParser(description="Simulate Gambler's ruin.")
    parser.add_argument('-N', type=int, help='Total amount of money between the two gamblers')
    arguments = parser.parse_args()
    arguments.N
    """


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
            if total_weight < 1 and i == len(tickers) - 1:
                weights[i] = weight
                print("Final stock reached, but total weight != 1. Increasing all weights.")
                return weights / total_weight
            if total_weight < 1: # the normal inputting
                weights[i] = weight
                continue
            if total_weight == 1 and i < len(tickers) - 1:
                weights[i] = weight
                print("Total weight of 1 reached. Assigning weight 0 to the rest.")
                return weights
            if total_weight == 1 and i == len(tickers) - 1: # end of normal inputting
                weights[i] = weight
                return weights
            if total_weight > 1:
                weights[i] = 1 - (total_weight - weight)
                print("Total weight is larger than 1. Truncating weights.")
                return weights / total_weight
    # equal or market cap weights
    specification = input("Market capitalization weights or 'equalweights'?")
    if specification.strip().lower() == 'equalweights':
        weights = [1 / len(tickers)] * len(tickers)
    else:
        weights = list(df.market_cap_weights(tickers).values())

    return weights


def generate_dashboard(returns, risk_contributions, sharpe_ratio, sortino_ratio, target_rate):
    """
    Generates a dashboard for portfolio analysis.

    Args:
        returns (pd.Series): Portfolio returns over time.
        risk_contributions (pd.DataFrame): DataFrame with risk contributions per asset.
        sharpe_ratio (float): The portfolio's Sharpe ratio.
        sortino_ratio (float): The portfolio's Sortino ratio.
        target_rate: (float): The target rate; e.g. the risk-free rate.
    """
    # Create main figure with adjusted layout
    _, axs = plt.subplots(4, 2, figsize=(20, 30))
    
    # pie chart
    vis.pie_risk_contributions(risk_contributions["Normalized Contribution"], axs[0, 0])
    axs[0, 0].set_title("Risk Contributions by Asset")
    
    # ratios in a textbox
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
    
    var = rm.value_at_risk(returns)
    cvar = rm.conditional_value_at_risk(returns)
    vis.plot_var_cvar(returns, var, cvar, axes=axs[2, 1])
    
    metrics = fs.monte_carlo_var(returns)
    projection = fs.simulate_future_returns(returns)
    vis.plot_simulations(projection, metrics['daily']['VaR'], metrics['daily']['CVaR'],
                         num_paths=3, axes=axs[3, 0])
    vis.plot_simulations_cumulative(projection, metrics['cumulative']['CVaR'],
                                    lower_pct=20, upper_pct=80, axes=axs[3, 1])
    
    plt.tight_layout(rect=[0, 0.05, 1, 1])  # ensures no overlap
    plt.show()


if __name__ == "__main__":
    main()