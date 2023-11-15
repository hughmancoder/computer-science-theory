package Factory.factoryPattern;

public class ConcreteProductA implements Product {
    @Override
    public void use() {
        System.out.println("Using Concrete Product A");
    }
}