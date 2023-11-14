// Source code is decompiled from a .class file using FernFlower decompiler.

import behaviours.FlyNoWay;
import behaviours.Quack;

public class ModelDuck extends Duck {
  public ModelDuck() {
    this.flyBehaviour = new FlyNoWay();
    this.quackBehaviour = new Quack();
  }

  public void display() {
    System.out.println("I'm a model duck.");
  }
}
