import java.util.List;

class PuzzlePiece {

    private Coordinate coordinate;
    // LEFT, TOP, RIGHT, BOTTOM when orientation = 0
    private List<Edge> edges;
    private int orientation; // 0, 90, 180, 270

    public PuzzlePiece(int x, int y, List<Edge> edges) {
        this.coordinate = new Coordinate(x, y);
        this.edges = edges;
        this.orientation = 0;
    }

    public void rotate() {
        orientation = (orientation + 90) % 360;
        Edge temp = edges.remove(0);
        edges.add(temp);
    }

    public int getOrientation() {
        return orientation;
    }

    public Coordinate getCoordinate() {
        return coordinate;
    }

    public List<Edge> getEdges() {
        return edges;
    }
}
