package Factory.abstractFactoryPattern;

public class ItalianPizza implements Pizza {
    public void prepare() {
        System.out.println("Preparing Italian Pizza");
    }

    public void bake() {
        System.out.println("Baking Italian Pizza");
    }

    public void serve() {
        System.out.println("Serving Italian Pizza");
    }
}
