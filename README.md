# Computer science theory

## Algorithms and Data Structures

- Algorithms and Data Structures are implemented in C++
- Design patterns are implemented in Java from the textbook Head First Design Patterns (O'Reilly second edition)

## Design patterns

## OO basics

Abstraction: Abstraction is the process of simplifying complex systems by representing only the essential features, hiding the implementation details. It allows you to focus on what an object does rather than how it does it, making it easier to understand and use.

Encapsulation: Encapsulation is the bundling of data (attributes) and methods (behaviors) that operate on that data within a single unit, known as a class. It hides the internal implementation of an object and allows access to its functionality through well-defined interfaces, promoting better code organization and security.

Polymorphism: Polymorphism allows objects of different classes to be treated as objects of a common superclass. It enables the use of a single interface to represent a group of related objects, making the code more flexible and extensible. Polymorphism can be achieved through method overriding and method overloading.

Inheritance: Inheritance is a mechanism where one class (subclass) acquires the properties and behaviors of another class (superclass). It promotes code reuse and enables the creation of hierarchies in which subclasses inherit characteristics from their parent classes, forming an "is-a" relationship.

## OO Principles

### Encapsulate What Varies

This principle is often summarized as "Identify the aspects of your application that vary and encapsulate them." It encourages you to isolate and contain parts of your code that are likely to change in the future. By doing so, you can make changes to specific components without affecting the entire system. This principle promotes modular design and helps in maintaining a clear separation of concerns.

### Favor Composition Over Inheritance

This principle suggests that you should prefer building new functionality by composing existing classes and components rather than relying heavily on class inheritance. While inheritance establishes an "is-a" relationship between classes, composition allows you to create more flexible and customizable interactions between objects. Composition allows you to assemble different behaviors without being tied to the constraints of a fixed inheritance hierarchy.

### Program to Interfaces, Not Implementations

This principle emphasizes designing your code to rely on interfaces (or abstract classes) rather than concrete implementations. By programming to interfaces, your code becomes more adaptable to changes. If you later need to replace a specific implementation with a different one, as long as they adhere to the same interface, the rest of your code doesn't need to change. This promotes flexibility and easier maintenance.

