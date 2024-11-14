"""Simulates coin tosses to show that the sequence HH occurs after HT on average.

We can also derive that result analytically, but since it's unintuitive at first glance
simulation does not hurt. The intuition is that for HT, once we get an H we made real progress:
Either we get a T and finish, or we get another H and are in the same position as before.
For HH, an initial H can still be reset to 0 if a T follows.

The program generates NUM_SEQUENCES many sequences of SEQUENCE_LENGTH length each. Then we
find the index of the completion of the sequences HH and HT, i. e., the index of the second
H and the index of the T respectively. To get the result from the source (below) or from how
we'd treat this analytically, I have to add 2 to the index: HH is completed on average after
6 tosses, HT after 4; the plus 2 gets us around zero-indexing and to the second position.
Inspired by Blitzstein; Hwang "Introduction to Probability." 2019. p. 442, 
but their code looks quite different.
"""

import numpy as np

# 1000 sequences of coin tosses, each of length 100
NUM_SEQUENCES = 10**4
SEQUENCE_LENGTH = 100
sequences = [''.join(np.random.choice(['H', 'T'], SEQUENCE_LENGTH, replace=True)) for _ in range(NUM_SEQUENCES)]

# first occurrences in each sequence
# first + 1 because of 0-indexing, and then another + 1 to get the second position
hh_positions = [seq.find("HH") + 1 + 1 if "HH" in seq else float('nan')
                for seq in sequences]
ht_positions = [seq.find("HT") + 1 + 1 if "HT" in seq else float('nan')
                for seq in sequences]

# mean waiting times
average_waiting_time_hh = np.nanmean(hh_positions)
average_waiting_time_ht = np.nanmean(ht_positions)
print("Average waiting time for HH:", average_waiting_time_hh)
print("Average waiting time for HT:", average_waiting_time_ht)
