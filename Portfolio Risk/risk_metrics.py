"""A set of helper functions to calculate various risk metrics for financial portfolios. 

The functions assume input returns are *daily* returns and require consistent formatting as Pandas 
Series. There are functions for Value at Risk (VaR), Conditional Value at Risk (CVaR), 
the Sharpe Ratio, the Sortino Ratio, and drawdowns.

Functions:
- `value_at_risk`: Calculates the Value at Risk (VaR) for a portfolio at a confidence level 
    using either the historical or parametric approach (assumes returns are Normal).
    That is the return the portfolio outperformed e.g. 95% of the time for the default value.
    
- `conditional_value_at_risk`: Calculates the Conditional VaR (CVaR) or 'Expected Shortfall,' 
    which represents the average loss for the returns below that VaR threshold.

- `sharpe_ratio`: Calculates the Sharpe Ratio, a risk-adjusted measure of returns relative to 
    a target rate (e.g. government bonds). Higher means better.

- `sortino_ratio`: Calculates the Sortino Ratio. Similar to Sharpe, but exclusively penalizing 
    negative returns relative to a target rate rather than all volatility. Higher means better.

- `drawdowns`: Calculates the drawdown for each point in time. That is, how far we are from the
    all time high right now in cumulative terms.
"""
import numpy as np
import pandas as pd
from scipy.stats import norm


def value_at_risk(returns: pd.Series, confidence_level: float = 0.95, method: str = 'historical') -> float:
    """
    Calculates the Value at Risk (VaR) for a portfolio at a specified confidence level.

    Parameters:
        returns (pd.Series): Daily portfolio returns.
        confidence_level (float): Confidence level for VaR (default is 95%).
        method (str): Method to calculate VaR ('historical' or 'parametric').

    Returns:
        float: The Value at Risk (negative value indicating potential loss).
    """
    if method == 'historical':
        return np.percentile(returns, (1 - confidence_level) * 100)
    if method == 'parametric':
        mean = returns.mean()
        std = returns.std()
        z_score = norm.ppf(1 - confidence_level)
        return mean - z_score * std
    raise ValueError("Invalid method. Choose 'historical' or 'parametric'.")


def conditional_value_at_risk(returns: pd.Series, confidence_level: float = 0.95) -> float:
    """
    Calculates the CVaR/Expected Shortfall for a portfolio at a specified confidence level.

    Parameters:
        returns (pd.Series): Daily portfolio returns.
        confidence_level (float): Confidence level for CVaR (default is 95%).

    Returns:
        float: The Conditional Value at Risk.
    """
    var = value_at_risk(returns, confidence_level, method='historical')
    return returns[returns <= var].mean()


def sharpe_ratio(returns: pd.Series, target_rate: float = 0.0) -> float:
    """
    Calculates the Sharpe Ratio for a portfolio given daily returns.

    Parameters:
        returns (pd.Series): Daily portfolio returns.
        target_rate (float): Daily target rate of return (default is 0.0).

    Returns:
        float: The Sharpe Ratio.
    """
    excess_returns = returns - target_rate
    return excess_returns.mean() / excess_returns.std()


def sortino_ratio(returns: pd.Series, target_rate: float = 0.0) -> float:
    """
    Calculates the Sortino Ratio for a portfolio given daily returns.

    Parameters:
        returns (pd.Series): Daily portfolio returns.
        target_rate (float): Daily target rate of return (default is 0.0).

    Returns:
        float: The Sortino Ratio.
    """
    excess_returns = returns - target_rate

    # np.minimum =/= np.min!
    downside_risk = np.sqrt((np.minimum(excess_returns, 0) ** 2).mean())
    return excess_returns.mean() / downside_risk


def drawdowns(returns: pd.Series) -> pd.Series:
    """
    Calculates drawdowns for a portfolio given daily returns.

    Parameters:
        returns (pd.Series): Daily portfolio returns.

    Returns:
        pd.Series: The drawdown for each day in the portfolio.
    """
    # no - 1 at the end since we're normalizing to the peak.
    # E.g., $200 peak and $150 trough => -25%, not -50%
    cumulative = (1 + returns).cumprod()
    
    # cummax gives a Series the length of 'cumulative' with
    # the max up to i in position i
    peak = cumulative.cummax()
    return (cumulative - peak) / peak

    # the maximum drawdown for 'returns' is, initially counterintuitively,
    # at: drawdowns(returns).min()
