# Trees and Graphs

4.1 Route Between Nodes
Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
Hints: None provided

4.2 Minimal Tree
Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height.

4.3 List of Depths
Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).

4.4 Check Balanced
Implement a function to check if a binary tree is balanced. For this question, a balanced tree is defined as one where the heights of the two subtrees of any node never differ by more than one.

4.5 Validate BST
Implement a function to check if a binary tree is a binary search tree.

4.6 Successor
Write an algorithm to find the "next" node (i.e., in-order successor: the next node for inorder traversal) of a given node in a binary search tree. Assume that each node has a link to its parent.

4.7 Build Order
You are given a list of projects and a list of dependencies (pairs of projects, where the second project is dependent on the first). Find a build order that allows the projects to be built. If there is no valid build order, return an error.
Example Input:
Projects: a, b, c, d, e, f
Dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
Output: f, e, a, b, d, c

4.8 First Common Ancestor
Design an algorithm to find the first common ancestor of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not necessarily a binary search tree.
Hints: #10, #16, #28, #36, #46, #70, #80, #96

4.9 BST Sequences
A binary search tree was created by traversing an array from left to right and inserting each element. Given a binary search tree with distinct elements, print all possible arrays that could have led to this tree.
Example Input:
Output: {2, 1, 3}, {2, 3, 1}
Hints: #39, #48, #66, #82

4.10 Check Subtree
T1 and T2 are two very large binary trees, with T1 much bigger than T2. Create an algorithm to determine if T2 is a subtree of T1.
Hints: #31

4.11 Random Node
Implement a binary tree class from scratch with methods insert, find, delete, and getRandomNode(), which returns a random node from the tree. All nodes should be equally likely to be chosen.
Hints: #42, #54, #62, #75, #89, #99, #112, #119

4.12 Paths with Sum
You are given a binary tree where each node contains an integer value. Design an algorithm to count the number of paths that sum to a given value. The path does not need to start or end at the root or a leaf but must go downwards.
Hints: #6, #14, #52, #68, #77, #87, #94, #103, #108, #115
