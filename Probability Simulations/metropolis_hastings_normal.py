"""A simple demonstration of the Normal–Normal conjugacy using Metropolis-Hastings.

From Blitzstein; Hwang "Introduction to Probability." 2019.
p. 544–48 for the math
p. 555–56 for the R code

We assume the conditional distribution of our Y data given theta is N(theta, sigma^2), 
but we don't know theta. Then we treat theta itself as an r.v. distributed N(mu, tau^2).
We can actually observe data Y, so we're interested in the posterior distribution of
theta|Y. We can solve this analytically, but another approach is to use the 
Metropolis-Hastings algorithm to construct a Markov chain whose stationary distribution
is that posterior distribution:
1.) Theta is currently in some state of the Markov chain. Then we first make a "proposal"
    for a new state by adding a normal r.v. with mean 0 and variance D^2. Values far from
    where we are are less likely to be proposed.
2.) We "accept" that proposal and actually move to that new state with a certain acceptance
    probability. This probability involves the probability that that state would be 
    proposed and the stationary probabilities. By symmetry, the proposal probabilities cancel
    and we end up with that ratio of the posterior distributions in the for-loop 
    we can deduce from Bayes' rule.
As we are bouncing around the Markov chain, more likely values for theta get visited more often
and the histogram of how often the values get visited becomes the posterior distribution we're
looking for. As it turns out, that is another Normal, hence the name Normal–Normal conjugacy.


The ratio of our prior uncertainty TAU about what the parameter is
and SIGMA determines how much our estimate of theta moves towards the observed data. 
Relatively large TAU like here and the mean zips to the observed data.
NUM_ITER controls how close the posterior distribution is to Normal; for 10,000 it looks 
very Normal (and the program takes around 10 seconds to run).
"""

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# parameters:
Y = 10      # observed data
SIGMA = 1   # SD of the data given the parameter

MU = 0      # mean of the prior Normal
TAU = 2     # SD of the prior Normal

D = 1       # proposal SD, mean assumed 0
NUM_ITER = 10**4

# Initialize theta with the observed value
theta = np.zeros(NUM_ITER)
theta[0] = Y

# loop for Metropolis-Hastings
for i in range(1, NUM_ITER):
    # propose new value for theta by adding a Normal r.v.
    theta_p = theta[i - 1] + np.random.normal(0, D)

    # the acceptance ratio r
    # see README or source above for where this is coming from
    r = (norm.pdf(Y, theta_p, SIGMA) * norm.pdf(theta_p, MU, TAU)) / \
        (norm.pdf(Y, theta[i-1], SIGMA) * norm.pdf(theta[i-1], MU, TAU))

    # accept or reject the proposal according to the ratio
    flip = np.random.binomial(1, min(r, 1))
    theta[i] = theta_p if flip == 1 else theta[i - 1]

# discard first half of the samples for burn-in
theta = theta[int(NUM_ITER / 2):]

# plotting histogram of the samples and actual Normal PDF
plt.hist(theta, bins=30, density=True, label="Sampled theta")
plt.plot(np.linspace(min(theta), max(theta), 1000),
         norm.pdf(np.linspace(min(theta), max(theta), 1000), loc=theta.mean(), scale=theta.std()),
         'r-', label="Actual Normal")
plt.xlabel('theta')
plt.title('Histogram of theta after burn-in')
plt.legend()

plt.show()
