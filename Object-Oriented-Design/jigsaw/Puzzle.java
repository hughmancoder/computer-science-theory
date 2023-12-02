import java.util.List;

public class Puzzle {
    private List<PuzzlePiece> pieces;
    private int size;
    private PuzzlePiece[][] board;

    public Puzzle(int size, List<PuzzlePiece> pieces) {
        this.size = size;
        this.pieces = pieces;
        this.board = new PuzzlePiece[size][size];
    }

    public void solveNaive() {
        for (PuzzlePiece piece : pieces) {
            for (int row = 0; row < size; row++) {
                for (int col = 0; col < size; col++) {
                    if (fitsAtPosition(piece, row, col)) {
                        board[row][col] = piece;
                        break;
                    }
                }
            }
        }
    }

    public PuzzlePiece[][] getBoard() {
        return board;
    }

    private boolean fitsAtPosition(PuzzlePiece piece, int row, int col) {
        return board[row][col] == null;
    }

}
