# Computer Science Theory

This repository is a comprehensive collection of code, theories, and examples spanning various domains of computer science from my undegraduate degree and additional learning

## Contents

### Algorithms-And-Data-Structures

- **Disjoint-Set**: Implementations of Quick-Find, Quick-Union, and Optimised Quick-Union
- **Hashtable**: Implementation of a hashtable using linear probing
- **Linked-List**: Implementation of a doubly linked list
- **Minimum-Spanning-Tree**: Kruskal's algorithm with deletion operation
- **Multiplication**: Karatsuba multiplication algorithm
- **Path-Finding**: Python implementation of a path-finding algorithm with test cases
- **Queue**: Circular queue and simple queue implementations
- **Sorting**: Merge sort implementation
- **Stack**: Basic stack implementation
- **Trees**: AVL and Binary Search Tree implementations

### Artificial-Intelligence

- **Hidden-Markov-Models**: Implementation of the Viterbi algorithm in Python
- **K-Mean-Clustering**: Kernel K-Mean clustering in a Jupyter notebook and theoretical explanation
- **Kd-Tree**: Nearest neighbour search using KD-tree
- **Support-Vector-Machines**: SVM implementation in a Jupyter notebook

### Computer-Systems

- **Assembly**: Assembly language programs with a focus on fundamental operations, sorting, and mathematical functions, including test cases and expected outputs
- **Virtual-Machine-Parser**: VMTranslator in Python, with test cases and compiled outputs

### Design-Patterns

- **Decorator**: Implementation of the decorator pattern in Java with a focus on a beverage example
- **Factory**: Factory pattern implementations with diagrams and Java code examples
- **Observer**: Weather station example using the observer pattern
- **Strategy**: Strategy pattern demonstrated through a duck simulation

### Object-Oriented-Design

- **Call-Center**: This project simulates a call center with multiple levels of employees (operator, supervisor, director). It handles incoming calls in an order of priority based on the employee's rank.

- **Chat-Server**: This project implements the boilerplate classes for a chat server. It allows multiple users to join a chat room, send messages, and see other users' messages in real time.

- **Deck-of-Cards**: This project simulates a deck of playing cards. It can shuffle the deck and deal cards. Classes are abstracted as much as possible for flexibility, and maintanability and specific card suites and ranks are delegated by enums.

- **File-System**: This project simulates a basic file system with directories and files. It supports operations like creating, reading, updating and deleting files and directories. The underlying data structure is an N-ary tree built with the composite design pattern which is acheived by Direcotry objects having a hashmap of child Directory objects and File objects. The files system manager suports operations such equivalent to linux commands such as cd, ls,rm, mkdir, touch, pwd.

- **Jigsaw**: This project simulates a jigsaw puzzle. It can check if a piece fits in a certain spot and can track the state of the puzzle with each edge beign identifiable as a corner, middle, or edge piece, with each edge having a unique shape and can have inset or outset protrusions. A naive recursive solution is implemented to solve the puzzle given a random scramble.

- **Minesweeper**: This project simulates the game of Minesweeper and is full featured and runs in the terminal. It generates a game board with mines placed in random locations and allows the player to make moves.

### System design

- **Cache-Design**

This document describes the design of a caching mechanism for a web server with 100 machines to respond to search queries. It discusses considerations such as distributed caching, cache invalidation, cache eviction policy, and load balancing.

- **Duplicate-URL**

This document discusses the design of a system to detect duplicate documents among 10 billion URLs with identical content. It covers considerations such as URL normalization, robots.txt, crawl depth, rate limiting, and handling real-world situations where some friends have more than others.

- **Pastebin**

This document describes the design of a system like Pastebin for generating random URLs to access user-entered text. It discusses considerations such as URL generation, text storage, data retrieval, and expiration.

- **Personal-Financial-Manager**

This document describes the design of a personal financial manager like Mint.com, connecting to bank accounts, analyzing spending habits, and making recommendations. It discusses considerations such as data integration, data analysis, recommendations, and security and privacy.

- **Sales-Rank**

This document describes the design of a system to list best-selling products overall and by category for a large eCommerce company. It discusses considerations such as data collection, data processing, data storage, and data presentation.

- **Social-Network**

This document describes the design of a social network system. It discusses considerations such as user management, friend management, post management, and news feed generation.

- **Stock-Data**

This document describes the design of a system to fetch and analyze stock data. It discusses considerations such as data fetching, data storage, data analysis, and data presentation.

- **Web-Crawler**

This document describes the design of a web crawler while avoiding infinite loops. It discusses considerations such as URL normalization, robots.txt, crawl depth, rate limiting, and handling real-world situations where some friends have more than others.
