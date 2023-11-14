// Source code is decompiled from a .class file using FernFlower decompiler.

import behaviours.FlyWithWings;
import behaviours.Quack;

public class MallardDuck extends Duck {
  public MallardDuck() {
    new Quack();
    new FlyWithWings();
  }

  public void display() {
    System.out.println("I'm a real Mallard duck");
  }
}
