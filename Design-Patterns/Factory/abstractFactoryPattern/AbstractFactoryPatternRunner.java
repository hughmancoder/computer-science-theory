package Factory.abstractFactoryPattern;

public class AbstractFactoryPatternRunner {
    public static void main(String[] args) {

        PizzaFactory factory = new ItalianPizzaFactory();
        PizzaStore store = new PizzaStore(factory);
        store.makePizza();
    }
}
