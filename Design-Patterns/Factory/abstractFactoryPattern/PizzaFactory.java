package Factory.abstractFactoryPattern;

public interface PizzaFactory {
    Pizza createPizza();

    Topping createTopping();
}
