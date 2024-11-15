from typing import Union
import yfinance as yf
import pandas as pd
import numpy as np

def process_data(tickers: list, start_date: str, end_date: str) -> pd.DataFrame:

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


def market_cap_weights(tickers: list) -> dict:
    
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

def cumulative_returns(daily_returns: pd.Series) -> pd.Series:
    
    # 1+ to the daily multiplier rather than percentage
    cumulative = (1 + daily_returns).cumprod() - 1
    return cumulative

# testing
tickers_test = ['AAPL', 'GOOG', 'MSFT']
weights_test = [0.5, 0.3, 0.2]

portfolio_returns_test = portfolio_returns(tickers_test, '2021-01-01', '2022-01-01', weights_test)

print(portfolio_returns_test)
print((cumulative_returns(portfolio_returns_test)))
# putting that into the same DataFrame:
#portfolio_daily_returns['Cumulative'] = cumulative_returns(portfolio_daily_returns)