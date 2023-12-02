import java.util.List;

class PuzzlePiece {
    String id;
    List<Edge> edges;
    private int orientation; // 0, 90, 180, 270

    public PuzzlePiece(int x, int y, List<Edge> edges) { // Corrected type of id to String
        this.id = x + ":" + y;
        this.orientation = 0;
    }

    public void rotate() {
        orientation = (orientation + 90) % 360;
        // remove from start and add to end
        Edge temp = edges.remove(0);
        edges.add(temp);
    }

    public String getId() {
        return id;
    }
}
