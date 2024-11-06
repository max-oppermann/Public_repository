""" 
Comparing differently sized simulations of the matching cards problem 
(cards numbered 1, ..., n; chance to at least once get card i that has i written on it).
Original idea (with only the 10^4 simulation and without plotting) in R-code from:
Blitzstein; Hwang "Introduction to Probability." 2019. p. 31.
"""

import numpy as np
import matplotlib.pyplot as plt

N = 100 # number of cards in the deck
NUM_REPLICATIONS = [10, 50, 250, 1250, 6250, 10**4]
np.random.seed(3)

proportions = []

# The loop creates one shuffled array 1 through N, one in order, then sums where they match.
# This creates a list with 'replications' many entries, each entry
# between 0 (no matches) and N (all matches).
for replications in NUM_REPLICATIONS:
    trials = [sum(
        np.random.choice(range(1, N + 1), N, replace=False)
        ==
        np.arange(1, N + 1)
        ) for _ in range(replications)]

    proportion = sum(matches >= 1 for matches in trials) / replications
    proportions.append(proportion)

# plotting
plt.figure(figsize=(10, 6))
plt.plot(NUM_REPLICATIONS, proportions, marker='o', color='b', label='Simulated Proportion')
plt.axhline(1 - 1 / np.e, color='r', linestyle='--', label=f'$1 - \frac{1}{np.e}$')
plt.xscale('log') # to make the beginning of the plot look less bunched up

plt.xlabel("Replications")
plt.ylabel("Proportion")
plt.legend()
plt.show()
