# Design Patterns

## Principles

### Encapsulate What Varies

Isolate parts of your code that are most likely to change, ensuring they have a single responsibility. This approach enhances maintainability and flexibility.

### Favor Composition Over Inheritance

Compose objects from other objects, rather than inheriting from a parent class, to promote greater flexibility and extendibility in your code.

### Program to Interfaces, Not Implementations

Focus on designing systems based on abstractions rather than concrete implementations. This principle increases modularity, flexibility, scalability, and makes the code more adaptable. It also facilitates easier testing and maintenance.

## Patterns

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

#### Factory Pattern

**Definition**: The Factory pattern is a creational design pattern that provides an interface for creating objects in a superclass but allows subclasses to alter the type of objects that will be created.

**Key Components**:

- **Creator**: An abstract class or interface with a method for creating objects.
- **ConcreteCreator**: A subclass that implements or overrides the method to create specific objects.
- **Product**: The interface or abstract class for the type of object the factory method will create.
- **ConcreteProduct**: The subclass of Product, which the factory method instantiates.

**Usage**:

- When the exact types of objects to be created are not known until runtime.
- To encapsulate object creation to keep it separate from the main business logic.

#### Abstract Factory Pattern

**Definition**: The Abstract Factory pattern is a creational design pattern that provides an interface for creating families of related or dependent objects without specifying their concrete classes.

**Key Components**:

- **AbstractFactory**: An interface with methods for creating a set of related products.
- **ConcreteFactory**: Specific classes that implement the AbstractFactory interface methods to create concrete products.
- **AbstractProduct**: An interface for a type of product object.
- **ConcreteProduct**: Classes that implement the AbstractProduct interface, representing specific products to be created by the concrete factory.
- **Client**: The class that uses the abstract factory and its products.

**Usage**:

- When there are interdependencies between the creation of various objects.
- To provide a way to configure a system with one of multiple families of products.

#### Factory vs Abstract Factory pattern

- Complexity and Scale: The Abstract Factory is more complex, dealing with families of products, while the Factory pattern is simpler, focusing on creating a single type of object.
- Level of Abstraction: Abstract Factory works at a higher level of abstraction, creating families of related objects, whereas the Factory pattern creates individual objects.
- Use Cases: The Factory pattern is used when it's necessary to encapsulate the logic of which concrete class to instantiate, while the Abstract Factory is used when the system needs to be independent of how its products are created, composed, and represented.
- Interdependencies: Abstract Factory handles the interdependencies between products, while the Factory pattern does not necessarily deal with multiple related products.

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
