"""Simulates the Gambler's Ruin problem and visualizes the results.

The logic of markov_chain_array() from:
Blitzstein; Hwang "Introduction to Probability." 2019. p. 523.

This program simulates a simplified version of the Gambler's Ruin problem, where one gambler 
starts with an initial amount of money and plays repeated rounds against an opponent with a 
specified probability of winning each round. The simulation stops early when the gambler either goes 
bankrupt or reaches the total amount of money available (the other gambler goes bankrupt). 
It then plots the progression of the gambler's money over time.

Command-line arguments can be used for the total amount of money, initial amount, probability 
of winning, and the number of rounds. If arguments are missing, the user gets prompted for input.

Usage:
    python gamblers_ruin.py -N <total_amount> -i <initial_amount> -p <probability> --nsim <num_sim>

Raises:
    ValueError: If any of the input parameters are nonsensical, 
                e.g. if the probability is not between 0 and 1.
"""

import argparse
import numpy as np
import matplotlib.pyplot as plt


def main(total_amount: int, initial_amount: int, prob: float, num_sim: int):
    """Simulates the Gambler's Ruin problem.

    Validates input arguments, generates the Markov chain of the gambler's money, 
    determines when the game ends, and visualizes the results.

    Args:
        total_amount (int): Total amount of money between the two gamblers.
        initial_amount (int): The amount of money our gambler starts with.
        prob (int): The probability that he will win a round.
        num_sim (int): The number of rounds to simulate.

    Raises:
        ValueError: If total_amount is less than initial_amount; one can't have more than the total.
        ValueError: If total_amount is not positive; no negative amounts of money.
        ValueError: If the prob is not between 0 and 1 inclusive.
        ValueError: If num_sim is negative; can't play less than no rounds.
    """
    # validation of input arguments
    if not total_amount >= initial_amount:
        raise ValueError(
            "Total amount of money N must be at least the initial amount i.")
    if not total_amount >= 0:
        raise ValueError("Total amount of money N must be positive.")
    if not 0 <= prob <= 1:
        raise ValueError("Probability p must be between 0 and 1.")
    if not num_sim >= 0:
        raise ValueError("Number of rounds nsim must be positive.")

    # getting the MC and when the game ends
    markov_chain = markov_chain_array(total_amount, initial_amount, prob, num_sim)
    stable_index = game_over_index(markov_chain, total_amount)
    
    # plotting
    lower_end = np.min(markov_chain)
    upper_end = np.max(markov_chain)

    _, ax = plt.subplots(figsize=(15, 8))
    ax.plot(markov_chain[:stable_index + 1])
    # complete labeling of axes only if not too many labels
    if stable_index <= 20:
        ax.set_xticks(np.arange(0, stable_index + 1, 1))
    if total_amount <= 20:
        ax.set_yticks(np.arange(0, total_amount + 1, 1))
    # zoom in if spread in MC small relative to possible range
    if upper_end - lower_end <= 20 and total_amount >= 60:
        ax.set_ylim(np.max(lower_end - 5, 0), np.min(upper_end + 5, 0))
    else:
        ax.set_ylim(0, total_amount)
    ax.set_xlim(0, stable_index + 1)
    ax.set_xlabel('Time Periods')
    ax.set_ylabel('Money')
    ax.set_title(f"Gambler's Ruin Simulation.\n Probability of winning a round: {prob}")

    plt.show()


def markov_chain_array(total_amount: int, initial_amount: int, prob: int, num_sim: int) -> np.ndarray:
    """Simulates the Markov chain representing the gambler's money over time.

    Args:
        total_amount (int): Total amount of money between the two gamblers.
        initial_amount (int): The amount of money our gambler starts with.
        prob (int): The probability that he will win a round.
        num_sim (int): The number of rounds to simulate.

    Returns:
        np.ndarray: NumPy array containing the gambler's amount of money at each step.
    """
    # initialize Markov chain
    markov_chain = np.zeros(num_sim, dtype=int)
    markov_chain[0] = initial_amount

    # simulate the Markov chain
    # not num_sim + 1 since we already filled the first spot in the array
    for j in range(1, num_sim):
        # one gambler is bankrupt
        if markov_chain[j-1] == 0 or markov_chain[j-1] == total_amount:
            markov_chain[j] = markov_chain[j-1]
        else:
            markov_chain[j] = markov_chain[j-1] + np.random.choice([1, -1], p=[prob, 1 - prob])
    return markov_chain


def game_over_index(m_c: np.ndarray, total_amount: int) -> int:
    """Determines the index when the game ends (when the gambler reaches 0 or the total amount).

    Args:
        m_c (np.ndarray): The Markov chain array representing the gambler's money over time.
        total_amount (int): Total amount of money between the two gamblers.

    Returns:
        int: Index at which the game ends (when 0 or total_amount is reached).
    """
    # condition in argmax gives an array of 0s and 1s
    # the index of the first of those gets returned by design of argmax. 
    # else condition makes sure the one that does not occur gets a larger number
    first_min_index = np.argmax(m_c == 0) if np.any(m_c == 0) else len(m_c)
    first_max_index = np.argmax(m_c == total_amount) if np.any(m_c == total_amount) else len(m_c)
    return min(first_min_index, first_max_index)


def get_input(args) -> tuple[int, int, float, int]:
    """Retrieves input arguments from the command line or interactively from the user.

    Args:
    - args: The parsed command-line arguments. With type indicator that would be 'args: Namespace'.

    Returns:
    - A tuple containing the total amount of money, initial amount for our gambler, 
        probability of winning a round, and number of rounds to be played.
    """
    
    if args.N is None or args.i is None or args.p is None or args.nsim is None:
        print("Missing command-line arguments. Please input values manually:")
        while True:
            try:
                total_amount = args.N if args.N is not None else int(
                    input("Enter total amount of money N: "))
                initial_amount = args.i if args.i is not None else int(
                    input("Enter initial amount for our gambler: "))
                prob = args.p if args.p is not None else float(
                    input("Enter probability our gambler wins each round: "))
                num_sim = args.nsim if args.nsim is not None else int(
                    input("Enter the number of rounds to simulate: "))
                break
            except ValueError:
                print("Invalid input. Please enter valid numbers only.")
    else:
        total_amount, initial_amount, prob, num_sim = args.N, args.i, args.p, args.nsim
    return total_amount, initial_amount, prob, num_sim


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simulate Gambler's ruin.")
    parser.add_argument('-N', type=int, help='Total amount of money between the two gamblers')
    parser.add_argument('-i', type=int, help='Initial amount for our gambler')
    parser.add_argument('-p', type=float, help='Probability our gambler wins')
    parser.add_argument('--nsim', type=int, help='Number of rounds to be played')

    arguments = parser.parse_args()

    N, i, p, nsim = get_input(arguments)

    main(N, i, p, nsim)
