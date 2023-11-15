package Factory.abstractFactoryPattern;

public class PizzaStore {
    private Pizza pizza;
    private Topping topping;

    public PizzaStore(PizzaFactory factory) {
        pizza = factory.createPizza();
        topping = factory.createTopping();
    }

    public void makePizza() {
        pizza.prepare();
        topping.addTopping();
        pizza.bake();
        pizza.serve();
    }
}
