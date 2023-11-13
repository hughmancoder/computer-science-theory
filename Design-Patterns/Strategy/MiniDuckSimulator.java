// Source code is decompiled from a .class file using FernFlower decompiler.
public class MiniDuckSimulator {
  public MiniDuckSimulator() {
  }

  public static void main(String[] var0) {
    MallardDuck var1 = new MallardDuck();
    var1.performQuack();
    var1.performFly();
    ModelDuck var2 = new ModelDuck();
    var2.performFly();
    var2.setFlyBehaviour(new FlyRocketPowered());
    var2.performFly();
  }
}
