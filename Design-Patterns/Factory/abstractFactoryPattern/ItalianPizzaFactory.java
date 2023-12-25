package Factory.abstractFactoryPattern;

public class ItalianPizzaFactory implements PizzaFactory {
    public Pizza createPizza() {
        return new ItalianPizza();
    }

    public Topping createTopping() {
        return new ItalianTopping();
    }
}
