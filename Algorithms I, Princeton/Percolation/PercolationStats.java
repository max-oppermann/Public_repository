import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;

public class PercolationStats {
    private int trials;
    private double[] results;

    // perform independent trials on an n-by-n grid
    public PercolationStats(int n, int trials) {
        if (n <= 0 || trials <= 0) {
            throw new IllegalArgumentException();
        }
        this.trials = trials;
        results = new double[trials];

        for (int i = 0; i < trials; i++) {
            Percolation perc = new Percolation(n);
            while (!perc.percolates()) {
                int randRow = StdRandom.uniformInt(1, n + 1);
                int randCol = StdRandom.uniformInt(1, n + 1);
                perc.open(randRow, randCol);
            }
            int openSites = perc.numberOfOpenSites();
            double fraction = (double) openSites / (n * n);
            results[i] = fraction;
        }
    }

    // sample mean of percolation threshold
    public double mean() {
        return StdStats.mean(results);
    }

    // sample standard deviation of percolation threshold
    public double stddev() {
        return StdStats.stddev(results);
    }

    // low endpoint of 95% confidence interval
    public double confidenceLo() {
        double mean = StdStats.mean(results);
        double SD = StdStats.stddev(results);
        double sqrtTrials = Math.sqrt(trials);
        return (mean - 1.96 * (SD / sqrtTrials));
    }

    // high endpoint of 95% confidence interval
    public double confidenceHi() {
        double mean = StdStats.mean(results);
        double SD = StdStats.stddev(results);
        double sqrtTrials = Math.sqrt(trials);
        return (mean + 1.96 * (SD / sqrtTrials));
    }

    // test client
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        int trials = Integer.parseInt(args[1]);

        // create PercolationStats object
        PercolationStats testPercStats = new PercolationStats(n, trials);

        double mean = testPercStats.mean();
        double SD = testPercStats.stddev();
        double ciLo = testPercStats.confidenceLo();
        double ciHi = testPercStats.confidenceHi();
        System.out.println("mean = " + mean);
        System.out.println("stddev = " + SD);
        System.out.printf("95%% confidence interval = [%.16f, %.16f]%n", ciLo, ciHi);

    }

}
