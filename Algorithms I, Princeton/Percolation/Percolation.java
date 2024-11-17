import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class Percolation {
    private boolean[][] openSites;
    private int numOpen;
    private WeightedQuickUnionUF uf;
    private int gridSize;
    private int virtualTop;
    private int virtualBottom;

    // creates n-by-n grid, with all sites initially blocked
    public Percolation(int n) {
        if (n <= 0) {
            throw new IllegalArgumentException("n must be greater than 0");
        }

        gridSize = n * n;
        openSites = new boolean[n][n];
        numOpen = 0;
        uf = new WeightedQuickUnionUF(gridSize + 2);

        virtualTop = gridSize;
        virtualBottom = gridSize + 1;
        // Connect virtual top to all sites in the top row
        for (int i = 0; i < n; i++) {
            uf.union(virtualTop, i);
        }
        // Connect virtual bottom to all sites in the bottom row
        for (int i = gridSize - n; i < gridSize; i++) {
            uf.union(virtualBottom, i);
        }
    }

    // opens the site (row, col) if it is not open already
    public void open(int row, int col) {
        if (!(row >= 1 && row <= Math.sqrt(gridSize) && col >= 1 && col <= Math.sqrt(gridSize))) {
            throw new IllegalArgumentException("Row and column indices must be between 1 and n.");
        }

        if (!isOpen(row, col)) // they get adjusted in isOpen()
        {
            int adjustedRow = row - 1;
            int adjustedCol = col - 1;
            openSites[adjustedRow][adjustedCol] = true;
            numOpen++;

            int index = convertTo1D(adjustedRow, adjustedCol);

            // Connect to adjacent open sites
            // union() still needs the adjusted rows and columns
            if (row > 1 && isOpen(row - 1, col)) {
                uf.union(index, convertTo1D(adjustedRow - 1, adjustedCol));
            }
            if (row < Math.sqrt(gridSize) && isOpen(row + 1, col)) {
                uf.union(index, convertTo1D(adjustedRow + 1, adjustedCol));
            }
            if (col > 1 && isOpen(row, col - 1)) {
                uf.union(index, convertTo1D(adjustedRow, adjustedCol - 1));
            }
            if (col < Math.sqrt(gridSize) && isOpen(row, col + 1)) {
                uf.union(index, convertTo1D(adjustedRow, adjustedCol + 1));
            }
        }
    }

    private int convertTo1D(int row, int col) {
        return row * (int) Math.sqrt(gridSize) + col;
    }

    // is the site (row, col) open?
    public boolean isOpen(int row, int col) {
        if (!(row >= 1 && row <= Math.sqrt(gridSize) && col >= 1 && col <= Math.sqrt(gridSize))) {
            throw new IllegalArgumentException("Row and column indices must be between 1 and n.");
        }

        int adjustedRow = row - 1;
        int adjustedCol = col - 1;
        return openSites[adjustedRow][adjustedCol];
    }

    // is the site (row, col) full?
    public boolean isFull(int row, int col) {
        if (!(row >= 1 && row <= Math.sqrt(gridSize) && col >= 1 && col <= Math.sqrt(gridSize))) {
            throw new IllegalArgumentException("Row and column indices must be between 1 and n.");
        }

        int adjustedRow = row - 1;
        int adjustedCol = col - 1;
        int site = convertTo1D(adjustedRow, adjustedCol);
        return uf.find(site) == virtualTop;
    }

    // returns the number of open sites
    public int numberOfOpenSites() {
        return numOpen;
    }

    // does the system percolate?
    public boolean percolates() {
        return uf.find(virtualTop) == uf.find(virtualBottom);
    }

    // test client (optional)
    public static void main(String[] args) {

        int n = 4;
        Percolation testPerc = new Percolation(n);
        testPerc.open(1, 1);
        testPerc.open(2, 1);
        testPerc.open(3, 1);
        testPerc.open(3, 2);
        testPerc.open(3, 3);
        testPerc.open(3, 4);
        testPerc.open(4, 4);

        System.out.println("Number of open sites: " + testPerc.numberOfOpenSites());
        System.out.println("Does the system percolate? " + testPerc.percolates());

    }
}
