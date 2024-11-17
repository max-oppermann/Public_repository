"""A set of helper functions to get and process data for financial portfolios.

Functions for analyzing financial portfolios using stock price data and custom weights. 
The functions use the yFinance library to fetch data and perform calculations for daily
portfolio returns and cumulative returns.

Functions:
- `process_data`: Downloads and preprocesses historical price data for a list of tickers.
- `get_target_rate`: User input for target rate of return for calculation of Sharpe/Sortino ratio.
- `market_cap_weights`: Calculates portfolio weights from market capitalizations (or equal weights).
- `portfolio_returns`: Computes daily portfolio returns from individual stock returns and weights.
- `cumulative_returns`: Computes cumulative returns of a portfolio from daily percentage changes.

Raises:
        ValueError: If the data can't be fetched properly or there are no tickers to fetch for.
"""

from typing import Union
import yfinance as yf
import pandas as pd
import numpy as np


def process_data(tickers: list, start_date: str, end_date: str) -> pd.DataFrame:
    """Fetches and preprocesses adjusted close price data for a list of tickers.

    Args:
        tickers (list): A list of stock ticker symbols (e.g., ['AAPL', 'MSFT']).
        start_date (str): The start date for the data fetch in 'YYYY-MM-DD' format.
        end_date (str): The end date for the data fetch in 'YYYY-MM-DD' format.

    Raises:
        ValueError: If the fetched data contains NaN values after preprocessing
                    or if the data is empty.

    Returns:
        pd.DataFrame: A DataFrame containing day-over-day percentage returns for each ticker.
    """

    fetch = yf.download(tickers, start=start_date, end=end_date)['Adj Close']

    # double filling to also get initial NaN values
    data = fetch.fillna(method='ffill').fillna(method='bfill')
    if data.isnull().values.any():
        raise ValueError("Data contains NaN values after preprocessing.")
    if data.empty:
        raise ValueError("No data fetched for the given tickers and dates.")

    # like data / data.shift(1) - 1
    returns = data.pct_change().dropna()
    return returns

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


def market_cap_weights(tickers: list) -> dict:
    """Calculates market capitalization-based weights for a portfolio of stocks.

    Retrieves the market capitalization for each ticker using 
    the yFinance library. If any market cap is missing, it defaults to the 
    average market cap of the other tickers. If all market caps are missing, 
    equal weights are assigned to all tickers.

    Parameters:
        tickers (list): A list of stock ticker symbols (e.g., ['AAPL', 'MSFT']).

    Returns:
        dict: A dictionary where keys are ticker symbols and values are their 
              respective portfolio weights based (hopefully) on market capitalization.

    Raises:
        ValueError: If the provided list of tickers is empty.
    """

    if not tickers:
        raise ValueError("Ticker list cannot be empty.")

    market_caps = {}
    weights = {}
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        market_caps[ticker] = stock.info.get('marketCap', 0)

    average_market_cap = np.sum(list(market_caps.values())) / len(tickers)

    # if they are all 0, equal weights
    if average_market_cap == 0:
        for ticker in tickers:
            weights[ticker] = 1 / len(tickers)
        return weights

    # if only some are 0, average market cap for those
    for ticker, cap in market_caps.items():
        if cap == 0:
            market_caps[ticker] = average_market_cap

    total_market_cap = np.sum(list(market_caps.values()))

    for ticker, cap in market_caps.items():
        weights[ticker] = cap / total_market_cap

    return weights


def portfolio_returns(tickers: list, start_date: str, end_date: str, weights: Union[list, str, None] = None) -> pd.Series:
    """Computes the daily returns of a portfolio of stocks.

    Processes historical price data for the given tickers, gets their daily returns, and 
    aggregates them into portfolio-level returns based on provided weights. If no weights 
    are provided, the function defaults to using market capitalization weights or equal weights.

    Parameters:
        tickers (list): A list of stock ticker symbols (e.g., ['AAPL', 'MSFT']).
        start_date (str): The start date for the historical data in 'YYYY-MM-DD' format.
        end_date (str): The end date for the historical data in 'YYYY-MM-DD' format.
        weights (Union[list, str, None], optional): 
            - A list of weights corresponding to the tickers.
            - 'equalweights' for equal weighting.
            - None (default) to use market capitalization weights.

    Returns:
        pd.Series: A time series of the portfolio day-over-day returns indexed by date.
    """

    individual_returns = process_data(tickers, start_date, end_date)

    # market cap weights if none provided
    # equal weights if keyword
    if weights is None:
        weights = list(market_cap_weights(tickers).values())
    elif weights == 'equalweights':
        weights = [1 / len(tickers)] * len(tickers)

    # underscore so my linter does not complain
    portfolio_returns_ = individual_returns.dot(weights)
    return portfolio_returns_


def cumulative_returns(daily_returns: Union[pd.Series, pd.DataFrame]) -> Union[pd.Series, pd.DataFrame]:
    """Computes the cumulative returns of a portfolio or multiple simulations of portfolio returns.

    Args:
        daily_returns (pd.Series or pd.DataFrame): 
            - A series of day-over-day portfolio returns for a single portfolio (1D).
            - A DataFrame where each row represents a simulation, and each column is a daily return.

    Returns:
        pd.Series or pd.DataFrame: 
            - If input is 1D, returns a series of cumulative portfolio returns up to each day.
            - If input is 2D, returns a DataFrame of cumulative returns for each simulation.
    """

    # multiple simulations (2D array), cumprod across axis=1
    if daily_returns.ndim == 2:
        # 1+ to the daily multiplier rather than percentage
        cumulative = (1 + daily_returns).cumprod(axis=1) - 1
    else:
        # a single portfolio (1D array)
        cumulative = (1 + daily_returns).cumprod() - 1
        
    return cumulative
