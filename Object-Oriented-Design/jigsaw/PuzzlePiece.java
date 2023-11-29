import java.util.List;

class PuzzlePiece {
    String id;
    List<Edge> edges;
    private int orientation; // 0, 90, 180, 270
    private boolean isPlaced;

    public PuzzlePiece(int id, List<Edge> edges) {
        this.id = id;
        this.edges = edges;
        this.orientation = 0;
        this.isPlaced = false;
    }

    public void rotate() {
        // Rotates the piece by 90 degrees clockwise and rearranges edges
        orientation = (orientation + 90) % 360;
        Edge temp = edges.remove(0);
        edges.add(temp);
    }
}