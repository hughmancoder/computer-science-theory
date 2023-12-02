import java.util.List;
import java.util.Collections;

public class Puzzle {
    private List<PuzzlePiece> pieces;
    private int size;
    private PuzzlePiece[][] board;

    public Puzzle(int size, List<PuzzlePiece> pieces) {
        this.size = size;
        this.pieces = pieces;
        this.board = new PuzzlePiece[size][size];

        scramblePieces();
    }

    private void scramblePieces() {
        // Randomize the order of the pieces
        Collections.shuffle(pieces);

        // Randomly rotate each piece
        for (PuzzlePiece piece : pieces) {
            int rotations = (int) (Math.random() * 4); // 0 to 3 rotations
            for (int i = 0; i < rotations; i++) {
                piece.rotate();
            }
        }
    }

    public void solveNaive() {
        // Reset the board
        for (int row = 0; row < size; row++) {
            for (int col = 0; col < size; col++) {
                board[row][col] = null;
            }
        }

        solveRecursive(0);
    }

    private boolean solveRecursive(int index) {
        if (index == pieces.size()) {
            return true;
        }

        PuzzlePiece piece = pieces.get(index);
        for (int row = 0; row < size; row++) {
            for (int col = 0; col < size; col++) {
                for (int rotation = 0; rotation < 4; rotation++) {
                    if (fitsAtPosition(piece, row, col)) {
                        board[row][col] = piece;
                        if (solveRecursive(index + 1)) {
                            return true;
                        }
                        // Remove the piece if it doesn't work
                        board[row][col] = null;
                    }
                    piece.rotate();
                }
            }
        }

        return false;
    }

    public PuzzlePiece[][] getBoard() {
        return board;
    }

    private boolean fitsAtPosition(PuzzlePiece piece, int row, int col) {
        // Check if the position is already occupied
        if (board[row][col] != null) {
            return false;
        }

        List<Edge> edges = piece.getEdges();
        int orientationShift = piece.getOrientation() / 90;

        // Calculate the index for each edge based on the orientation
        int leftEdgeIndex = (0 + orientationShift) % 4;
        int topEdgeIndex = (1 + orientationShift) % 4;
        int rightEdgeIndex = (2 + orientationShift) % 4;
        int bottomEdgeIndex = (3 + orientationShift) % 4;

        // Check LEFT edge
        if (col > 0 && board[row][col - 1] != null) {
            Edge leftEdge = edges.get(leftEdgeIndex);
            Edge rightEdgeOfNeighbor = board[row][col - 1].getEdges().get(2); // Right edge of the left neighbor
            if (!leftEdge.fitsWith(rightEdgeOfNeighbor)) {
                return false;
            }
        }

        // Check TOP edge
        if (row > 0 && board[row - 1][col] != null) {
            Edge topEdge = edges.get(topEdgeIndex);
            Edge bottomEdgeOfNeighbor = board[row - 1][col].getEdges().get(3); // Bottom edge of the top neighbor
            if (!topEdge.fitsWith(bottomEdgeOfNeighbor)) {
                return false;
            }
        }

        // Check RIGHT edge
        if (col < size - 1 && board[row][col + 1] != null) {
            Edge rightEdge = edges.get(rightEdgeIndex);
            Edge leftEdgeOfNeighbor = board[row][col + 1].getEdges().get(0); // Left edge of the right neighbor
            if (!rightEdge.fitsWith(leftEdgeOfNeighbor)) {
                return false;
            }
        }

        // Check BOTTOM edge
        if (row < size - 1 && board[row + 1][col] != null) {
            Edge bottomEdge = edges.get(bottomEdgeIndex);
            Edge topEdgeOfNeighbor = board[row + 1][col].getEdges().get(1); // Top edge of the bottom neighbor
            if (!bottomEdge.fitsWith(topEdgeOfNeighbor)) {
                return false;
            }
        }

        // The piece fits in the position
        return true;
    }

}