package Decorator;

import Decorator.condiments.*;

// Coffee Shop
public class Main {
        public static void main(String args[]) {
                Beverage beverage = new DarkRoast();
                System.out.println(beverage.getDescription()
                                + " $" + beverage.cost());

                Beverage beverage2 = new DarkRoast();
                beverage2 = new Mocha(beverage2);
                beverage2 = new Milk(beverage2);
                System.out.println(beverage2.getDescription()
                                + " $" + beverage2.cost());

                Beverage beverage3 = new Decaf();
                beverage3 = new Soy(beverage3);
                System.out.println(beverage3.getDescription()
                                + " $" + beverage3.cost());
        }
}
