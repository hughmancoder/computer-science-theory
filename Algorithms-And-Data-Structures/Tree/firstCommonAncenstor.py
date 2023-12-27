import unittest

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def findFirstCommonAncestor(root, node1, node2):
    return dfs(root, node1, node2)

def dfs(node, node1, node2):
    if node is None:
        return None

    if node == node1 or node == node2:
        # Found one of the nodes
        return node

    left = dfs(node.left, node1, node2)
    right = dfs(node.right, node1, node2)

    if left and right:
        # If both left and right subtree return a node, current node is the common ancestor
        return node

    # If only one of the left or right subtree returns a node, pass that node up
    return left if left is not None else right


if __name__ == "__main__":
    root = TreeNode('root')
    node1 = TreeNode('node1')
    node2 = TreeNode('node2')
    node3 = TreeNode('node3')
    node4 = TreeNode('node4')

    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4

    ancestor = findFirstCommonAncestor(root, node3, node4)
    print(f"Common ancestor of node3 and node4 is: {ancestor.value}")

    # Example 2
    node5 = TreeNode('node5')
    node2.left = node5

    ancestor = findFirstCommonAncestor(root, node5, node4)
    print(f"Common ancestor of node5 and node4 is: {ancestor.value}")

    # Example 3
    node6 = TreeNode('node6')
    node4.right = node6

    ancestor = findFirstCommonAncestor(root, node6, node3)
    print(f"Common ancestor of node6 and node3 is: {ancestor.value}")