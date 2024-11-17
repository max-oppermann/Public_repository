import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.MinPQ;
import edu.princeton.cs.algs4.StdOut;

import java.util.ArrayList;
import java.util.List;

public class Solver {
    private final List<SearchNode> solutionPath;
    private final boolean solvable;

    private static class SearchNode implements Comparable<SearchNode> {
        public final Board board;
        public final int moves;
        public final int manhattan;
        public final SearchNode previous;

        public SearchNode(Board board, int moves, SearchNode previous) {
            this.board = board;
            this.moves = moves;
            this.manhattan = board.manhattan();
            this.previous = previous;
        }

        @Override
        public int compareTo(SearchNode other) {
            return Integer.compare((this.moves + this.manhattan), (other.moves + other.manhattan));
        }
    }


    // find a solution to the initial board (using the A* algorithm)
    public Solver(Board initial) {
        if (initial == null) {
            throw new IllegalArgumentException();
        }
        boolean solvable1 = false;

        Board twinBoard = initial.twin();
        SearchNode initialTwin = new SearchNode(twinBoard, 0, null);
        SearchNode initialOriginal = new SearchNode(initial, 0, null);

        MinPQ<SearchNode> twinPQ = new MinPQ<>();
        MinPQ<SearchNode> originalPQ = new MinPQ<>();

        solutionPath = new ArrayList<>();

        originalPQ.insert(initialOriginal);
        SearchNode minNode = originalPQ.min();
        if (minNode.board.isGoal()) {
            solutionPath.add(minNode);
        }
        twinPQ.insert(initialTwin);
        SearchNode minTwin = twinPQ.min();

        while (!minNode.board.isGoal() && !minTwin.board.isGoal()) {
            minNode = originalPQ.delMin();
            minTwin = twinPQ.delMin();
            solutionPath.add(minNode);

            for (Board neighbor : minNode.board.neighbors()) {
                if (minNode.previous == null || !neighbor.equals(minNode.previous.board)) {
                    SearchNode neighborNode = new SearchNode(neighbor, minNode.moves + 1, minNode);
                    originalPQ.insert(neighborNode);
                }
            }
            for (Board neighborTwin : minTwin.board.neighbors()) {
                if (minTwin.previous == null || !neighborTwin.equals(minTwin.previous.board)) {
                    SearchNode neighborNodeTwin = new SearchNode(neighborTwin, minTwin.moves + 1,
                                                                 minTwin);
                    twinPQ.insert(neighborNodeTwin);
                }
            }
        }
        // checking the last element in the solutionPath; it will only be the goal board
        // if the minNode.board.isGoal() condition became true.
        if (solutionPath.get(solutionPath.size() - 1).board.isGoal()) {
            solvable1 = true;
        }
        solvable = solvable1;
    }


    // is the initial board solvable?
    public boolean isSolvable() {
        return solvable;
    }

    // min number of moves to solve initial board; -1 if unsolvable
    public int moves() {
        if (!isSolvable()) {
            return -1;
        }
        return solutionPath.get(solutionPath.size() - 1).moves;
    }


    // sequence of boards in a shortest solution; null if unsolvable
    public Iterable<Board> solution() {
        if (!isSolvable()) {
            return null;
        }

        List<Board> boards = new ArrayList<>();
        SearchNode currentNode = solutionPath.get(
                solutionPath.size() - 1); // Start from the goal node
        while (currentNode != null) {
            boards.add(0,
                       currentNode.board); // Add boards to the beginning of the list to maintain correct order
            currentNode = currentNode.previous; // Move to the previous node
        }

        return boards;
    }


    // test client (see below)
    public static void main(String[] args) {

        // create initial board from file
        In in = new In(args[0]);
        int n = in.readInt();
        int[][] tiles = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                tiles[i][j] = in.readInt();
        Board initial = new Board(tiles);

        // solve the puzzle
        Solver solver = new Solver(initial);

        // print solution to standard output
        if (!solver.isSolvable())
            StdOut.println("No solution possible");
        else {
            StdOut.println("Minimum number of moves = " + solver.moves());
            for (Board board : solver.solution())
                StdOut.println(board);
        }
    }

}
