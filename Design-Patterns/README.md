# Design patterns

## Principles

### Encapsulate What Varies

isolate parts of your code that are most likely to change to have a single responsibility. This helps with maintainability and flexibility

### Favor Composition Over Inheritance

Favour composing objects of other objects rather than inhereting a class from a parent class

### Program to Interfaces, Not Implementations

Design systems based on abstractions rather than concrete implementations. This principle enhances modularity, flexibility, and scalability and makes code more adaptable and facilitates easier testing and maintenance.

## Design Patterns

### Strategy Pattern

The Strategy pattern is a behavioral design pattern that enables selecting an algorithm's behaviour at runtime. Instead of implementing a single algorithm directly, code receives run-time instructions as to which in a family of algorithms to use.

**Core Components**:

- **Strategy Interface**: An interface common to all supported algorithms.
- **Concrete Strategy**: Implements the strategy interface with a specific algorithm.
- **Context**: Maintains a reference to a strategy object and is configured with a concrete strategy object to call the algorithm defined by the strategy.

Example Application: Paxos distributed System where server can act as a proposer, acceptor or a learner

### Observer pattern

Defines a one to many dpendency between objects so that when once changes, all dependednt are notified and updated automatically

Example: news paper subscription with publisher as subct and subscribers as observer

### Factory Pattern

The Factory pattern is a creational design pattern used to create objects. Instead of directly invoking a constructor, an interface is used for creating an object, but the choice of which class to instantiate is deferred to subclasses.

**Core Components**:

- **Creator**: An abstract class or interface that declares the factory method, which returns an object of a product class.
- **Concrete Creator**: Implements or extends the creator class and overrides the factory method to return an instance of a specific product.
- **Product**: An interface or abstract class that defines the object the factory method will create.
- **Concrete Product**: Implements or extends the product interface or class. The factory method instantiated in the concrete creator returns this.

### Mediator Pattern

The Mediator pattern is a behavioral design pattern that reduces the direct communication between objects by having them communicate instead through a mediator object. This centralizes complex communications and control between related objects.

**Core Components**:

- **Mediator Interface**: An interface that defines the communication rules between objects.
- **Concrete Mediator**: Implements the mediator interface and coordinates communication between colleague objects. It knows and maintains its colleagues.
- **Colleagues**: Objects that communicate with each other through the mediator object.

### Singleton Pattern

The Singleton pattern is a creational pattern that ensures a class has only one instance and provides a global point of access to it.

**Core Components**:

- **Singleton Class**: A class that ensures only a single instance of itself is created. It provides a static method that returns this instance, creating it on the first call.

### Running the program

Refer to makefile
