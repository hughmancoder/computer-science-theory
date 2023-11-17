import behaviours.FlyBehaviour;
import behaviours.FlyWithWings;
import behaviours.Quack;
import behaviours.QuackBehaviour;

public abstract class Duck {
  /* Object composition */
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