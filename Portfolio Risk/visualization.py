"""A set of helper functions to visualize portfolio performance. 

The functions plot historical daily returns, historical cumulative returns, historical drawdowns, 
Monte Carlo simulated future daily and cumulative returns. Both historical and simulated are
accompanied by Value at Risk (VaR) and Conditional Value at Risk (CVaR).
They require an Axes object and each function returns the object with the plot, allowing for
further customization if desired.

Functions:
- `ax_setup`: Utility to return a new Matplotlib Axes object in the first place.
- `set_plot_labels`: Utility to set labels and title of an Axes object.
- `plot_historical_returns`: Plot daily portfolio returns over time.
- `plot_cumulative_returns`: Plot cumulative portfolio returns over time.
- `plot_drawdowns`: Plot portfolio drawdowns over time.
- `plot_var_cvar`: Plot a histogram of historical returns with VaR and CVaR.
- `plot_simulations`: Plot a subset of simulated returns with VaR and CVaR.
- `plot_simulations_cumulative`: Plot cumulative simulated returns with CIs and CVaR.
"""

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
import numpy as np
import pandas as pd

import risk_metrics as rm
import datafetch as df


def ax_setup() -> Axes:
    """Utility to return a Matplotlib Axes object.

    Returns:
        Axes: Matplotlib Axes object to modify.
    """
    return plt.subplots(figsize=(10, 6))[1]


def set_plot_labels(title: str, xlabel: str, ylabel: str, axes: Axes):
    """Set labels for a matplotlib Axes object.

    Args:
        title (str): Title of the plot.
        xlabel (str): Label for the x-axis.
        ylabel (str): Label for the y-axis.
        ax (matplotlib.axes.Axes): Matplotlib Axes object to modify.
    """
    axes.set_title(title)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel)
    axes.legend()
    axes.grid(alpha=0.4)


def plot_historical_returns(returns: pd.Series, axes: Axes = None) -> Axes:
    """Plot daily portfolio returns over time for historical data.

    Args:
        returns (pd.Series): Historical daily portfolio returns.
        ax (matplotlib.axes.Axes): Axis to plot on. If None, creates a new figure and axis.

    Returns:
        Axes: The matplotlib Axes object with the plot.
    """
    if axes is None:
        axes = ax_setup()

    axes.plot(returns, label="Daily Returns", color="blue", alpha=0.8)
    axes.axhline(0, color='black', linewidth=0.8, linestyle='--', alpha=0.7)
    set_plot_labels("Historical daily portfolio returns",
                    "Date",
                    "Returns", axes)
    return axes


def plot_cumulative_returns(returns: pd.Series, axes: Axes = None) -> Axes:
    """Plot cumulative portfolio returns over time for historical data.

    Args:
        returns (pd.Series): Historical daily portfolio returns.
        ax (matplotlib.axes.Axes): Axis to plot on. If None, creates a new figure and axis.

    Returns:
        Axes: The matplotlib Axes object with the plot.
    """
    if axes is None:
        axes = ax_setup()

    cumulative_values = df.cumulative_returns(returns)
    axes.plot(cumulative_values, label="Cumulative Returns", color="green", alpha=0.8)
    set_plot_labels("Historical cumulative portfolio returns",
                    "Date",
                    "Cumulative returns", axes)
    return axes


def plot_drawdowns(returns: pd.Series, axes: Axes = None) -> Axes:
    """Plot portfolio drawdowns over time for historical data.

    Args:
        returns (pd.Series): Historical daily portfolio returns.
        ax (matplotlib.axes.Axes): Axis to plot on. If None, creates a new figure and axis.

    Returns:
        Axes: The matplotlib Axes object with the plot.
    """
    if axes is None:
        axes = ax_setup()

    drawdown_values = rm.drawdowns(returns)
    axes.plot(drawdown_values, label="Drawdowns", color="red", alpha=0.8)
    axes.fill_between(drawdown_values.index, drawdown_values, 0, color='red', alpha=0.2)
    set_plot_labels("Portfolio Drawdowns", "Date", "Drawdown", axes)
    return axes


def plot_var_cvar(returns: pd.Series, var: float, cvar: float, axes: Axes = None) -> Axes:
    """Plot historical portfolio returns as a histogram with VaR and CVaR.

    Args:
        returns (pd.Series): Historical daily portfolio returns.
        var (float): Historical Value at Risk.
        cvar (float): Historical Conditional Value at Risk.
        ax (matplotlib.axes.Axes): Axis to plot on. If None, creates a new figure and axis.

    Returns:
        Axes: The matplotlib Axes object with the plot.
    """
    if axes is None:
        axes = ax_setup()

    axes.hist(returns, bins=50, color="blue", alpha=0.8, edgecolor="k", label="Historical Returns")
    axes.axvline(var, color="orange", linestyle="--", linewidth=1, label=f"VaR ({var:.2%})")
    axes.axvline(cvar, color="red", linestyle="--", linewidth=1, label=f"CVaR ({cvar:.2%})")
    set_plot_labels("VaR and conditional VaR for the historical data",
                    "Return",
                    "Frequency", axes)
    return axes


def plot_simulations(simulated_returns: np.ndarray, var: float, cvar: float, num_paths=3,
                     axes: Axes = None) -> Axes:
    """Plot a random subset of simulated daily returns to visualize variability, and the C/VaR.

    Args:
        simulated_returns (np.ndarray): Simulated daily returns (2D).
        num_paths (int): Number of random simulation paths to plot.
        var (float): Monte Carlo derived Value at Risk.
        cvar (float): Monte Carlo derived Conditional Value at Risk.
        ax (matplotlib.axes.Axes): Axis to plot on. If None, creates a new figure and axis.

    Returns:
        Axes: The matplotlib Axes object with the plot.
    """
    if axes is None:
        axes = ax_setup()

    sampled_paths = simulated_returns[np.random.choice(simulated_returns.shape[0],
                                                       num_paths,
                                                       replace=False), :]
    for path in sampled_paths:
        axes.plot(path, alpha=0.8)

    axes.axhline(var, color="orange", linestyle="--", linewidth=1, label=f"VaR ({var:.2%})")
    axes.axhline(cvar, color="red", linestyle="--", linewidth=1, label=f"CVaR ({cvar:.2%})")
    set_plot_labels(f"Sample of {num_paths} simulated daily return paths",
                    "Days in the future",
                    "Returns", axes)
    return axes


def plot_simulations_cumulative(simulated_returns: np.ndarray, cvar: float, lower_pct: int = 5,
                                upper_pct: int = 95, axes: Axes = None) -> Axes:
    """Plot CIs for cumulative returns over the simulation period and the CVaR for those returns.

    Args:
        cumulative_returns (np.ndarray): Simulated cumulative returns (2D).
        cvar (float): Monte Carlo Conditional Value at Risk.
        ax (matplotlib.axes.Axes): Axis to plot on. If None, creates a new figure and axis.
        lower_pct (int): Lower bound for the CI.
        upper_pct (int): Upper bound for the CI.

    Returns:
        Axes: The matplotlib Axes object with the plot.
    """
    if axes is None:
        axes = ax_setup()

    cum_returns = df.cumulative_returns(simulated_returns)
    days = np.arange(cum_returns.shape[1])
    percentiles = [lower_pct, 50, upper_pct]
    stats = np.percentile(cum_returns, percentiles, axis=0)

    axes.axhline(cvar, color="red", linestyle="--", linewidth=1, label=f"CVaR ({cvar:.2%})")
    axes.fill_between(days, stats[0], stats[2], color="blue", alpha=0.4,
                    label=f"{lower_pct}%-{upper_pct}% CI")
    axes.plot(days, stats[1], color="pink", label="Median")
    set_plot_labels("Simulated cumulative returns with CIs",
                    "Days in the future",
                    "Cumulative Returns", axes)
    return axes
