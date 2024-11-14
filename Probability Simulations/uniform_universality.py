"""
Showcases the universality of the Uniform: Transforming Unif(0,1) numbers via an
inverse CDF creates r.v.s that have the distribution of r.v.s that have that (not inverse) CDF.
Also, plugging an r.v. into its own CDF generates uniformly random numbers on (0,1).

All of this is inspired by the following lines of R code
u <- runif(10^4)
x <- log(u/(1-u))
hist(x)
from Blitzstein; Hwang "Introduction to Probability." 2019. p. 254–55.
The inverse functions are also covered in that book.
"""

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import logistic, norm, expon, rayleigh

U = np.random.uniform(0, 1, 10**4)
X_VALS = np.linspace(-10, 10, 1000)


def main():
    """Handles the input arguments, selects the distribution, and plots the results."""

    distributions = {
        "logistic": (logistic, "Logistic"),
        "normal": (norm, "Normal"),
        "rayleigh": (rayleigh, "Rayleigh"),
        "exponential": (expon, "Exponential")
    }
    # getting the distribution
    # default to Exponential if no argument or "invalid" argument
    if len(sys.argv) > 1:
        dist, name = distributions.get(sys.argv[1], (expon, "Exponential"))
    else:
        dist, name = expon, "Exponential"

    # getting the values
    pdf_vals, uniform_sim, pdf_sim = universality_values(dist)

    # plotting
    _, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    ax1.hist(pdf_sim, bins=50, density=True, alpha=0.6, color='blue')
    ax1.plot(X_VALS, pdf_vals, 'r-', lw=2, label=f"Actual {name} PDF")
    ax1.set_title(f"Plugging Uniform into inverse of {name}")
    ax1.legend()

    ax2.hist(uniform_sim, bins=50, density=True, alpha=0.6, color='green')
    ax2.set_title(f"Plugging {name} into its own CDF")

    plt.tight_layout()
    plt.show()


def universality_values(dist=None):
    """
    Computes values for plotting the universality of the Uniform.

    This function calculates
    (a) The theoretical PDF of the desired distribution via the .pdf() method that comes with scipy.
    (b) A simulation of the Uniform on (0,1) via the .cdf() method applied 
        to r.v.s of the same distribution.
    (c) A simulation of the CDF of the desired distribution via plugging the Uniform into
        the reverse CDF of that distribution.

    Parameters:
    dist : scipy.stats distribution object
        A distribution from scipy.stats, either logistic, norm, expon, or rayleigh.

    Returns:
    tuple : (pdf_vals, uniform_sim, pdf_sim)
        - pdf_vals: (a) above
        - uniform_sim: (b) above
        - pdf_sim: (c) above
    """

    # the theoretical dist (red line in plot)
    pdf_vals = dist.pdf(X_VALS)

    # plugging r.v. into its own CDF
    uniform_sim = dist.cdf(dist.rvs(size=20**4))

    # plugging the Uniform into inverse CDFs
    pdf_sim = None  # Initialize to None to avoid UnboundLocalError

    if dist == logistic:
        pdf_sim = np.log(U / (1 - U))
    elif dist == norm:
        pdf_sim = norm.ppf(U)  # no simple analytic expression
    elif dist == expon:
        pdf_sim = -np.log(1 - U)
    elif dist == rayleigh:
        pdf_sim = np.sqrt(-2 * np.log(1 - U))
    return pdf_vals, uniform_sim, pdf_sim


if __name__ == "__main__":
    main()