# Design Patterns

## Principles

### Encapsulate What Varies

Isolate parts of your code that are most likely to change, ensuring they have a single responsibility. This approach enhances maintainability and flexibility.

### Favor Composition Over Inheritance

Compose objects from other objects, rather than inheriting from a parent class, to promote greater flexibility and extendibility in your code.

### Program to Interfaces, Not Implementations

Focus on designing systems based on abstractions rather than concrete implementations. This principle increases modularity, flexibility, scalability, and makes the code more adaptable. It also facilitates easier testing and maintenance.

## Design Patterns

### Strategy Pattern

A behavioral design pattern that allows the selection of an algorithm's behavior at runtime. Instead of implementing a single algorithm, code receives run-time instructions on which algorithm to use from a family of algorithms.

**Core Components**:

- **Strategy Interface**: Common interface for all supported algorithms.
- **Concrete Strategy**: Specific implementation of the strategy interface.
- **Context**: Maintains a reference to a strategy object and is configured with a concrete strategy to execute the algorithm.

**Example Application**: Paxos distributed System where a server can act as a proposer, acceptor, or learner.

### Observer Pattern

Defines a one-to-many dependency between objects. An object, known as the subject, notifies all dependent objects, known as observers, of any state changes. Useful where changes to one object require updates in others.

### Decorator Pattern

Dynamically attaches additional responsibilities to an object, providing a flexible alternative to subclassing for extending functionality. Enhances or modifies the behavior of individual objects at runtime without altering their classes.

### Factory Pattern

A creational design pattern used to create objects via an interface. It defers the choice of which class to instantiate to subclasses.

**Core Components**:

- **Creator**: Abstract class or interface declaring the factory method.
- **Concrete Creator**: Implements or extends the creator, overriding the factory method.
- **Product**: Interface or abstract class for the object created by the factory method.
- **Concrete Product**: Implements or extends the product interface or class.

### Mediator Pattern

A behavioral pattern that reduces direct communication between objects through a mediator object. Centralizes complex communications and controls between related objects.

**Core Components**:

- **Mediator Interface**: Defines communication rules between objects.
- **Concrete Mediator**: Implements the mediator interface, coordinating communication.
- **Colleagues**: Objects communicating through the mediator.

### Singleton Pattern

Ensures a class has only one instance and provides a global point of access to it.

**Core Components**:

- **Singleton Class**: Ensures only a single instance is created, with a static method to access it.

### Running the Program

Refer to the provided makefile for instructions on compiling and running the program.
