package Factory.factoryPattern;

public class ConcreteFactoryA implements Factory {
    @Override
    public Product createProductA() {
        return new ConcreteProductA();
    }

    public Product createProductB() {
        return new ConcreteProductB();
    }
}
