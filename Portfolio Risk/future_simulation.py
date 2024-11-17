"""A set of helper functions to simulate future returns and risk for financial portfolios.

This module contains functions to simulate future daily returns and cumulative returns of 
a portfolio based on historical performance and to calculate risk metrics (VaR and CVaR).

Functions:
- `simulate_future_returns`: Simulates future daily returns using a normal distribution 
    based on historical returns data.
- `monte_carlo_var`: Uses future simulations to calculate the VaR CVaR for both daily 
    and cumulative returns over a specified period.
"""

import numpy as np
import pandas as pd

import datafetch as df
import risk_metrics as rm

def simulate_future_returns(returns: pd.Series, num_sim: int = 10000, num_days: int = 252) -> np.ndarray:
    """Simulate future daily returns using a Normal distribution based on historical parameters.

    Parameters:
        returns (pd.Series): Historical daily portfolio returns.
        num_sim (int): Number of simulations to run (default is 10,000).
        num_days (int): Number of days to simulate (default is 252, one trading year).

    Returns:
        np.ndarray: Simulated daily returns (shape: num_simulations x num_days).
    """
    mean = returns.mean()
    std = returns.std()
    return np.random.normal(loc=mean, scale=std, size=(num_sim, num_days))


def monte_carlo_var(returns: pd.Series, num_sim: int = 10000, num_days: int = 252, confidence_level: float = 0.95) -> dict:
    """Perform Monte Carlo simulations to calculate VaR and CVaR for daily and cumulative returns.

    Parameters:
        returns (pd.Series): Historical daily portfolio returns.
        num_sim (int): Number of simulations to run (default is 10,000).
        num_days (int): Number of days to simulate (default is 252, one trading year).
        confidence_level (float): Confidence level for VaR/CVaR

    Returns:
        dict: Dictionary containing VaR and CVaR results for the daily returns and 
            the cumulative returns at the end of the num_days period.
    """
    simulated_daily_returns = simulate_future_returns(returns, num_sim, num_days)
    simulated_cumulative_returns = df.cumulative_returns(simulated_daily_returns)

    # VaR and CVaR for both
    var_daily = rm.value_at_risk(simulated_daily_returns, confidence_level)
    cvar_daily = rm.conditional_value_at_risk(simulated_daily_returns, confidence_level)

    # final cumulative returns for all 10,000 paths
    # since shape is num_simulations x num_days
    final_cumulative_returns = simulated_cumulative_returns[:, -1]
    var_cumulative = rm.value_at_risk(final_cumulative_returns, confidence_level)
    cvar_cumulative = rm.conditional_value_at_risk(final_cumulative_returns, confidence_level)


    return {
        "daily": {"VaR": var_daily, "CVaR": cvar_daily},
        "cumulative": {"VaR": var_cumulative, "CVaR": cvar_cumulative},
        }
