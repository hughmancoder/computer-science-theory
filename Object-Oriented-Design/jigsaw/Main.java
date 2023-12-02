import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<PuzzlePiece> pieces = new ArrayList<>();
        int Size = 4;
        int totalPieces = Size * Size;
        for (int i = 0; i < totalPieces; i++) {
            List<Edge> edges = new ArrayList<>();

            // Each piece has 4 edges
            for (int j = 0; j < 4; j++) {
                // Randomly assigning edge shapes for demonstration
                Edge.Shape shape = Edge.Shape.values()[(int) (Math.random() * Edge.Shape.values().length)];
                edges.add(new Edge(shape));
            }

            // coordinates
            int x = i / Size;
            int y = i % Size;

            pieces.add(new PuzzlePiece(x, y, edges));
        }

        int size = 4;
        Puzzle puzzle = new Puzzle(size, pieces);
        puzzle.solveNaive();

        // Output or display the solved puzzle
        System.out.println("Solved Puzzle Layout:");
        for (int row = 0; row < size; row++) {
            for (int col = 0; col < size; col++) {
                PuzzlePiece piece = puzzle.getBoard()[row][col];
                System.out.print((piece != null ? piece.getId() : "Empty") + "\t");
            }
            System.out.println();
        }
    }
}
