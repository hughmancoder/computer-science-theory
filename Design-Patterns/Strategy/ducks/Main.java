import behaviours.FlyRocketPowered;

public class Main {
    public static void main(String[] args) {
        // Create a Mallard Duck
        Duck mallard = new MallardDuck();
        mallard.performQuack();
        mallard.performFly();

        // Create a Model Duck
        Duck model = new ModelDuck();
        model.performFly();
        model.setFlyBehaviour(new FlyRocketPowered());
        model.performFly();
    }
}
