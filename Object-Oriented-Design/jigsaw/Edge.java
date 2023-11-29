public class Edge {
    public enum EdgeType {
        INNER, OUTER, FLAT
    }

    private EdgeType type;
    private int partnerId; // ID of the edge this edge fits with

    public Edge(EdgeType type) {
        this.type = type;
    }

    public boolean fitsWith(Edge other) {
        // TODO
        return false;
    }
}
