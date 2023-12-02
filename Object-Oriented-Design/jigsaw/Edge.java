public class Edge {
    public enum Shape {
        INNER, OUTER, FLAT
    }

    private Shape shape;
    private int partnerId;

    public Edge(Shape shape) {
        this.shape = shape;
    }

    public boolean fitsWith(Edge other) {
        if (this.shape == Shape.FLAT && other.shape == Shape.FLAT) {
            return true;
        } else if (this.shape == Shape.INNER && other.shape == Shape.OUTER) {
            return true;
        } else if (this.shape == Shape.OUTER && other.shape == Shape.INNER) {
            return true;
        }
        return false;
    }
}
