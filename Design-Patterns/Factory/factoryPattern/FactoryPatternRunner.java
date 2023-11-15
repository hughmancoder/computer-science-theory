package Factory.factoryPattern;

public class FactoryPatternRunner {
    public static void main(String[] args) {
        Factory factoryA = new ConcreteFactoryA();
        Product productA = factoryA.createProductA();
        Product productB = factoryA.createProductB();
        productA.use();
        productB.use();

    }
}
