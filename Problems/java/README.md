# Java

### 13.1 Private Constructor

**Effect of Keeping a Constructor Private in Terms of Inheritance**

- A private constructor in a class prevents it from being instantiated outside of the class itself. This also means that the class cannot be subclassed, as the subclass would need to invoke the constructor of its superclass.

### 13.2 Return from Finally

**Does the `finally` block get executed if a `return` statement is inside the `try` block of a `try-catch-finally`?**

- Yes, the `finally` block is executed even if there's a `return` statement in the `try` block. The `finally` block executes after the `try` and `catch` blocks but before any `return` statements in the `try` block.

### 13.3 Final, Finally, and Finalize

**Difference Between `final`, `finally`, and `finalize`**

- `final` is a keyword used to declare constants, prevent method overriding, or prevent inheritance.
- `finally` is a block that complements a `try-catch` block, ensuring code within it is always executed regardless of exceptions.
- `finalize` is a method that is called by the garbage collector on an object when garbage collection determines that there are no more references to the object.

### 13.4 Generics vs. Templates

**Explain the Difference Between Templates in C++ and Generics in Java**

- Templates in C++ are a compile-time mechanism that allows code to operate with different data types. Generics in Java are similar but involve type erasure, which means type checking is done at compile time, and the type information is removed at runtime.

### 13.5 TreeMap, HashMap, LinkedHashMap

**Differences Between TreeMap, HashMap, and LinkedHashMap**

- `TreeMap` stores key-value pairs in a sorted order. It's based on the red-black tree structure.
- `HashMap` stores key-value pairs in a hash table, providing constant-time complexity for basic operations, assuming the hash function disperses the elements properly.
- `LinkedHashMap` maintains a linked list of entries in the map, in the order in which they were inserted. This allows it to maintain an iteration order, which is normally the order in which keys were inserted.

### 13.6 Object Reflection

**Explain What Object Reflection is in Java and Why it is Useful**

- Object reflection in Java allows an executing program to examine or "introspect" upon itself, and manipulate internal properties of the program. It is useful for cases where the program needs to dynamically load classes, call methods, or access fields without knowing these at compile time.

### 13.7 Lambda Expressions

**Usage of Lambda Expressions in Java**

- Lambda expressions are a feature in Java that allows you to implement methods of a functional interface more concisely. They are used extensively in functional programming and stream operations.
- Example:
  ```java
  List<String> list = Arrays.asList("a", "b", "c");
  list.forEach(e -> System.out.println(e));
  ```
