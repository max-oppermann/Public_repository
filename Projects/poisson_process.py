"""Simulates and visualizes a Poisson process via exponential interarrival times.

Generates arrival times for a Poisson process with a specified rate and duration.
Arrival times are generated from exponential interarrival times and visualized on a timeline.

The meat of the program (creating the Poisson process) is a translation of 4 lines of R code from 
Blitzstein; Hwang "Introduction to Probability." 2019. p. 255.

Command-line Arguments:
    - `--rate`: The event arrival rate (λ) of the Poisson process (default: 5).
    - `--end_time`: The maximum time until which to simulate arrivals (default: 10).
    
Example usage:
    python poisson_process.py.py --rate 10 --end_time 15
"""
import argparse
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon


def main(rate, end_time):
    """Creates and plots the arrival times of a Poisson process via Exponentials."""

    arrival_times = poisson_process(rate, end_time)
    plot_poisson(rate, end_time, arrival_times)


def poisson_process(rate: int, end_time: int) -> np.ndarray:
    """Generates arrival times for a Poisson process given a rate and duration.

    Args:
        rate (int): Event rate of the Poisson process.
        end_time (int): Maximum time duration for the process.

    Returns:
        np.ndarray: Array of arrival times, truncated at `end_time`.
    """

    # on average there will be rate * end_time many arrivals, rest is safety buffer
    interarrival_times = expon.rvs(scale=1/rate, size=int(rate * end_time * 1.5))
    arrival_times = np.cumsum(interarrival_times)

    # cut off excess times that won't be displayed
    arrival_times = arrival_times[arrival_times < end_time]
    return arrival_times


def plot_poisson(rate: int, end_time: int, arrival_times: np.ndarray):
    """Plots the arrival times of a Poisson process on a timeline.

    Args:
        rate (int): Rate of the Poisson process that was simulated.
        end_time (int): Maximum time until which the process was simulated.
        arrival_times (ndarray): Array of arrival times in the Poisson process.
    """

    # adjust the figsize to pull apart the marks
    _, ax = plt.subplots(figsize=((rate + end_time) * 1.2, 2))

    ax.scatter(arrival_times, [0.5] * len(arrival_times),
               marker='x', color='black', s=40)
    ax.axhline(0.5, color='gray', linestyle='-', linewidth=1)

    ax.set_xlabel('Time')
    ax.set_title(f'Poisson Process with rate {rate}')
    ax.set_yticks([])  # suppressing ticks on y-axis

    # force matplotlib to display a tick for each time period
    ax.set_xticks(np.arange(0, end_time + 1, 1))
    ax.grid(linestyle='--', alpha=0.6)

    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simulate a Poisson process.')
    parser.add_argument('--rate', type=int, default=5, help='Rate (lambda) of the Poisson process')
    parser.add_argument('--end_time', type=int, default=10, help='End time for the simulation')

    args = parser.parse_args()
    main(args.rate, args.end_time)
