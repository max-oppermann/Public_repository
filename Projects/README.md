Programs of varying length and complexity without intentional theme (currently the theme is probability theory).

#### `gamblers_ruin.py`  
Simulates a setup of the Gambler's Ruin problem as a Markov chain. Two gamblers with each an initial amount of money play a series of rounds with a fixed probability of winning one additional unit of money each round from the other gambler. If gambler A has probability $p$ of winning, gambler B has probability $(1-p)$ of winning; if the total money is $N$ and gambler A starts with $i$, gambler B has $(N-i)$. The simulation assumes the perspective of one of the gamblers. It then tracks the gambler's balance over time until they either go bankrupt (reach 0) or reach the total amount in play (the sum of both gamblers' money), i. e., until the other gambler goes bankrupt. The path of the gambler's money is then plotted.  
You can run the program from the command line with the following parameters: `N` (total amount of money), `i` (initial amount of money our gambler has), `p` (probability that he wins a round), `nsim` (number of rounds to simulate at the max; game may end before but not after). E. g.:  
`python gamblers_ruin.py -N 100 -i 50 -p 0.45 --nsim 1000`

#### `matching_cards.py`
Simulates the matching cards problem: Shuffle a deck of $N$ cards, labeled 1 through $N$. What is the probability that at least one card in position $i$ has $i$ written on it (turning over the seventh card and it has a 7 on it, e. g., but also drawing 1, 2, 3, 4, ...)?  
Solving this analytically gives $1-\frac1e\approx0.63$, which is in fact what the program converges to for simulating the problem often enough. "Often enough" turns out to be at least 10,000 times. I also plot the convergence behavior from 10 to 10,000 replications.  

#### `metropolis_hastings_normal.py`  
A simple demonstration of the Normal–Normal conjugacy using Metropolis-Hastings.  
We have a two-level model:  
$\theta\sim\mathcal N(\mu,\tau^2)$  
$Y|\theta\sim\mathcal N(\theta,\sigma^2)$  
with an unknown $\theta$. The Normal–Normal conjugacy is just that $\theta|Y\sim\mathcal N(\cdot,\cdot)$ with some complicated parameters; the point is that the posterior distribution is also Normal, just like the prior. By Bayes' rule we know that the posterior PDF  
$f_{\theta|Y}(\theta|Y)\propto f_{Y|\theta}(y|\theta)f_\theta(\theta)$  
since the prior distribution of $Y$ in the denominator does not depend on $\theta$. That in turn is proportional to  
$e^{-\frac12\left(\frac{y-\theta}\sigma\right)^2} \times e^{-\frac12\left(\frac{\theta-\mu}\tau\right)^2}$  
since both of those PDFs are Normal with those parameters by assumption. Now we can solve for the sought posterior distribution analytically. But we can also simulate it via Markov chain Monte Carlo. That is what this program does and the above derivation is relevant for the formula in the for–loop, since it turns out the acceptance probability of moving from state $x$ to a proposed state $x'$ is  
$\min\left(\frac{f_{\theta|Y}(x'|y)}{f_{\theta|Y}(x|y)},1\right)$  

#### `monty_hall.py`  
Simulates the classic Monty Hall problem, allowing you to play multiple rounds. The car is randomly placed behind one of three doors, you are asked to choose one. After your choice, Monty reveals a non-car door, and you are given the option to switch. The program tracks your wins and losses, and also compares your results with theoretical probabilities of winning by always staying or always switching (simulates 1000 rounds of always staying/switching). The simulation continues until you decide to stop.

#### `poisson_process.py`  
Simulates and visualizes a Poisson process using exponential interarrival times. The process has an event arrival rate $\lambda$ and runs for a specified time interval. The simulation generates interarrival times as i.i.d. $\text{Exponential}(\lambda)$ r.v.s. The cumulative sum of these interarrival times gives the arrival times in the Poisson process, which are then truncated at the specified end time. The arrival times are plotted on a timeline.  
The rate and end time can be modified in the command line, they default to 5 and 10 respectively:  
`python poisson_process.py --rate 10 --end_time 15`

#### `uniform_universality.py`  
Demonstrates the universality of the Uniform distribution:
- Inverse CDF + Uniform: By transforming uniformly random variables – $\text{Unif}(0,1)$ – through the inverse CDF of a chosen distribution, it generates random variables that follow the target distribution's shape.
- CDF + r.v.s of the same distribution: By applying the CDF of a chosen distribution to its own random variables, it produces uniformly random values on (0,1).  

Supports four distributions: Logistic, standard Normal, Exponential(1), and Rayleigh. It compares the theoretical PDF with a simulation generated using the transformation outlined above via visual plots of the results.

#### `weather_analysis.ipynb`  
Under construction.