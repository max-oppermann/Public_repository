"""Monte Carlo integration to estimate the value of pi.

We generate different numbers of points in the plane in the square [-1,1]x[-1,1].
The ratio of points in the unit circle to the total number of points approaches the
ratio of the area of the unit circle to the area of that square, which is pi/4.
Plotting the estimates thus derived shows convergence to the real value of pi for
larger and larger simulations.

R code from Blitzstein; Hwang "Introduction to Probability." 2019. p. 484–85.
"""
import numpy as np
import matplotlib.pyplot as plt

NUM_POINTS = [10**i for i in range(2, 7)]

estimates = np.zeros(len(NUM_POINTS))
for i, number in enumerate(NUM_POINTS):
    x_values = np.random.uniform(-1, 1, number)
    y_values = np.random.uniform(-1, 1, number)
    
    # multiply by 4 since there are 4 quadrants of area 1,
    # so without the 4 this approaches pi/4
    estimates[i] = 4*np.sum(x_values**2 + y_values**2 < 1)/number
    

plt.plot(NUM_POINTS, estimates, marker='o')
plt.hlines(np.pi, 0, NUM_POINTS[-1], colors='red', linestyles='dashed')
plt.xscale('log')
plt.show()