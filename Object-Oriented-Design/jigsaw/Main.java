import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<PuzzlePiece> pieces = new ArrayList<>();
        int size = 4;
        int totalPieces = size * size;

        // Initialize puzzle pieces
        for (int i = 0; i < totalPieces; i++) {
            List<Edge> edges = new ArrayList<>();

            // Each piece has 4 edges
            for (int j = 0; j < 4; j++) {
                // Randomly assigning edge shapes for demonstration
                Edge.Shape shape = Edge.Shape.values()[(int) (Math.random() * Edge.Shape.values().length)];
                edges.add(new Edge(shape));
            }

            // Coordinates
            int x = i / size;
            int y = i % size;

            pieces.add(new PuzzlePiece(x, y, edges));
        }

        // Create and solve the puzzle
        Puzzle puzzle = new Puzzle(size, pieces);
        puzzle.solveNaive(); // Assuming this is your solving method

        // Output the solved puzzle layout
        System.out.println("Solved Puzzle Layout:");
        for (int row = 0; row < size; row++) {
            for (int col = 0; col < size; col++) {
                PuzzlePiece piece = puzzle.getBoard()[row][col];

                if (piece != null) {
                    Coordinate coordinate = piece.getCoordinate();
                    System.out.print("[" + coordinate.x + "," + coordinate.y + "] ");
                } else {
                    System.out.print("[  ] ");
                }
            }
            System.out.println();
        }
    }
}
