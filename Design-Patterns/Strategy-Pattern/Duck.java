// Source code is decompiled from a .class file using FernFlower decompiler.
public abstract class Duck {
  protected FlyBehaviour flyBehaviour = new FlyWithWings();
  protected QuackBehaviour quackBehaviour = new Quack();

  public Duck() {
  }

  public abstract void display();

  public void performFly() {
    if (this.flyBehaviour != null) {
      this.flyBehaviour.fly();
    }

  }

  public void performQuack() {
    if (this.quackBehaviour != null) {
      this.quackBehaviour.quack();
    }

  }

  public void swim() {
    System.out.println("All ducks float, even decoys!");
  }

  public void setFlyBehaviour(FlyBehaviour var1) {
    this.flyBehaviour = var1;
  }

  public void setQuackBehaviour(QuackBehaviour var1) {
    this.quackBehaviour = var1;
  }
}
