"""Simulates a version of Winner's Curse with variable thresholds for when the bid gets accepted.

Inspired by Blitzstein; Hwang "Introduction to Probability." 2019. p. 441–42.
Their R code is quite different, but the logic how `accepted_bids` gets created is theirs.

There is a mystery prize of some value that is at least 0 and at most 1.
You can make a bid for the prize, but it is only accepted if it meets a threshold of 
the actual prize value. If the threshold is above 0.5, your best bet is not to play! 
The expected value of the prize – conditional on the fact that your bid was accepted – is then
negative for all positive bids. This maybe counterintuitive result is demonstrated here:

The program simulates 200 bids between 0 and 1 for a (float) threshold that can be passed in as
a command line argument. For each bid a large number of prize values are generated uniformly 
at random. The expected payoff for that bid is then the mean of the values for when the bid was 
accepted minus the bid you have to pay. These results of expected payoffs are plotted against the 
bid values. The bid with the highest expected payoff is highlighted.

Something goes wrong when the number of BID_VALUES is too close to NUM_SIM:
You get some positive payouts for thresholds larger than 0.5, which is mathematically impossible. 
"""
import sys
import numpy as np
import matplotlib.pyplot as plt

THRESHOLD = float(sys.argv[1]) if len(sys.argv) > 1 else 2/3

# to avoid the quirk of mathematically impossible positive payoffs,
NUM_SIM = int(10000 * 1 / (2 * np.abs(THRESHOLD - 0.5))
              ) if THRESHOLD != 0.5 else 10000

RESULTS = np.zeros(200)
BID_VALUES = np.linspace(0, 1, 200)

for i, bid in enumerate(BID_VALUES):
    value = np.random.uniform(0, 1, NUM_SIM)  # values of mystery prizes
    accepted_bids = value[bid > THRESHOLD * value]

    # only calculate mean payoff if accepted_bids is non-empty.
    # code works without it, but this suppresses a warning.
    if accepted_bids.size > 0:
        RESULTS[i] = np.mean(accepted_bids) - bid
    else:
        RESULTS[i] = float('nan')

max_index = np.nanargmax(RESULTS)
plt.scatter(BID_VALUES, RESULTS, s=5)
plt.scatter(BID_VALUES[max_index], RESULTS[max_index], color="red", s=15, label="Max payoff")

plt.hlines(0, 0, 1, colors="red", linestyles="dashed")
plt.vlines(BID_VALUES[max_index], ymin=plt.ylim()[0], ymax=RESULTS[max_index], colors="green", linestyles="dashed")

plt.xlabel("Bid")
plt.ylabel("Expected payoff")

plt.legend()
plt.show()
