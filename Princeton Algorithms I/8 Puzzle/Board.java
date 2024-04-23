import java.util.ArrayList;
import java.util.List;

public class Board {

    private final int[][] tiles;
    private final int dimension;

    public Board(int[][] tiles) {
        this.tiles = copy(tiles);
        this.dimension = tiles.length;
    }

    // defensive copy; the thing is supposed to be immutable
    private int[][] copy(int[][] original) {
        int[][] copy = new int[original.length][];
        for (int i = 0; i < original.length; i++) {
            copy[i] = original[i].clone();
        }
        return copy;
    }

    // potential ERROR source? adding the empty space
    // string representation of this board
    public String toString() {
        String boardString = Integer.toString(this.dimension) + "\n";
        for (int i = 0; i < this.dimension; i++) {
            for (int j = 0; j < this.dimension; j++) {
                boardString += tiles[i][j] + " ";
            }
            boardString += "\n";
        }
        return boardString;
    }

    // board dimension n
    public int dimension() {
        return dimension;
    }

    // number of tiles out of place
    public int hamming() {
        int hammingDistance = 0;
        for (int i = 0; i < this.dimension; i++) {
            for (int j = 0; j < this.dimension; j++) {
                // skip the blank field; it shouldn't count towards distance
                if (tiles[i][j] != 0 && tiles[i][j] != i * this.dimension + j + 1) {
                    hammingDistance++;
                }
            }
        }
        return hammingDistance;
    }

    // sum of Manhattan distances between tiles and goal
    public int manhattan() {
        int manhattanDistance = 0;
        for (int i = 0; i < this.dimension; i++) {
            for (int j = 0; j < this.dimension; j++) {
                int tileValue = tiles[i][j];
                // same as above, skip blank tile
                if (tileValue != 0) {
                    int goalRow = (tileValue - 1) / this.dimension;
                    int goalCol = (tileValue - 1) % this.dimension;
                    manhattanDistance += Math.abs(i - goalRow) + Math.abs(j - goalCol);
                }
            }
        }
        return manhattanDistance;
    }

    // is this board the goal board?
    public boolean isGoal() {
        return hamming() == 0;
    }

    // does this board equal y?
    public boolean equals(Object y) {
        if (y == this) {
            return true;
        }
        if (y == null) {
            return false;
        }
        if (!y.getClass().equals(Board.class)) {
            return false;
        }
        Board that = (Board) y;
        if (this.dimension != that.dimension) {
            return false;
        }
        for (int i = 0; i < this.dimension; i++) {
            for (int j = 0; j < this.dimension; j++) {
                if (this.tiles[i][j] != that.tiles[i][j]) {
                    return false;
                }
            }
        }
        return true;
    }

    // all neighboring boards
    public Iterable<Board> neighbors() {
        List<Board> neighborBoards = new ArrayList<>();

        int blankRow = -1;
        int blankCol = -1;
        for (int i = 0; i < this.dimension; i++) {
            for (int j = 0; j < this.dimension; j++) {
                if (tiles[i][j] == 0) {
                    blankRow = i;
                    blankCol = j;
                    break;
                }
            }
            // the other break only breaks out of the inner-loop
            if (blankRow != -1) {
                break;
            }
        }

        int[][] directions = { { 0, 1 }, { 1, 0 }, { 0, -1 }, { -1, 0 } };
        for (int[] dir : directions) {
            int row = blankRow + dir[0];
            int col = blankCol + dir[1];
            if (row >= 0 && row < this.dimension && col >= 0 && col < this.dimension) {
                int[][] newTiles = copy(this.tiles);
                // swap the tiles if it's a valid position
                int temp = newTiles[blankRow][blankCol];
                newTiles[blankRow][blankCol] = newTiles[row][col];
                newTiles[row][col] = temp;

                neighborBoards.add(new Board(newTiles));
            }
        }

        return neighborBoards;
    }

    // a board that is obtained by exchanging any pair of tiles
    public Board twin() {
        int[][] twin = copy(this.tiles);
        if (twin[0][0] != 0 && twin[0][1] != 0) {
            int temp = twin[0][0];
            twin[0][0] = twin[0][1];
            twin[0][1] = temp;
        }
        // if the 0 is either of those two, it won't be in the second row
        else {
            int temp = twin[1][0];
            twin[1][0] = twin[1][1];
            twin[1][1] = temp;
        }

        return new Board(twin);
    }

    // unit testing (not graded)
    public static void main(String[] args) {
        int[][] tiles = { { 1, 0, 3 }, { 4, 5, 6 }, { 7, 8, 2 } };
        Board board = new Board(tiles);

        System.out.println("Original:");
        System.out.println(board.toString());
        System.out.println("Dimension: " + board.dimension());
        System.out.println("Hamming: " + board.hamming());
        System.out.println("Manhattan: " + board.manhattan());
        System.out.println("Goal Board? " + board.isGoal());

        int[][] sameTiles = { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 0 } };
        Board sameBoard = new Board(sameTiles);
        System.out.println("Are boards equal? " + board.equals(sameBoard));

        System.out.println("Neighbors:");
        Iterable<Board> neighbors = board.neighbors();
        for (Board neighbor : neighbors) {
            System.out.println(neighbor.toString());
        }

        // Test twin() method
        Board twinBoard = board.twin();
        System.out.println("Twin:");
        System.out.println(twinBoard.toString());
    }


}
