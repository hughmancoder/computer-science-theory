# OO Problems

1. **Deck of Cards**: Design the data structures for a generic deck of cards. Explain how you would subclass the data structures to implement blackjack.

2. **Call Center**: Imagine you have a call center with three levels of employees: respondent, manager, and director. Design the classes and data structures for this problem. Implement a method `dispatchCall()` which assigns a call to the first available employee.

3. **Jigsaw**: Implement an NxN jigsaw puzzle. Design the data structures and explain an algorithm to solve the puzzle. You can assume that you have a `fitsWith` method which, when passed two puzzle edges, returns true if the two edges belong together.

Analysis:

Sorting Phase: O(N²) as we iterate through all pieces and their edges.
Assembly Phase: Potentially O(N⁴), considering each piece and possible orientation for each position.
Optimisations: Pruning (skipping unfitting pieces early), caching (remembering failed configurations), and parallel processing (solving different puzzle sections concurrently) can reduce the time complexity.

4. **Chat Server**: Explain how you would design a chat server. In particular, provide details about the various backend components, classes, and methods. What would be the hardest problems to solve?

5. **Minesweeper**: Design and implement a text-based Minesweeper game.

6. **File System**: Explain the data structures and algorithms that you would use to design an in-memory file system. Illustrate with an example in code where possible.
