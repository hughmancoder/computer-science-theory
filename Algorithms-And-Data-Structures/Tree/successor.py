class TreeNode:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

"""Returns the next largest node in the tree"""
def findInorderSuccessor(node):
    # get left most node of right subtree
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node

    # otherwise return the parent value to the right of current value
    parent = node.parent
    while parent is not None and parent.right == node:
        node = parent
        parent = parent.parent
    return parent
        


if __name__ == "__main__":
    # Construct a BST with parent links that reflects the tree in the image
    root = TreeNode(20)
    root.left = TreeNode(8, parent=root)
    root.right = TreeNode(22, parent=root)
    root.left.left = TreeNode(4, parent=root.left)
    root.left.right = TreeNode(12, parent=root.left)
    root.left.right.left = TreeNode(10, parent=root.left.right)
    root.left.right.right = TreeNode(14, parent=root.left.right)

    """
          20
       /  \
      8   22
     / \
    4  12
       /  \
      10   14
    
    In the above diagram, inorder successor of 8 is 10, inorder successor of 10 is 12 and inorder successor of 14 is 20.
    """

    
    node_8 = root.left
    node_10 = root.left.right.left
    node_14 = root.left.right.right

    result_node_8 = findInorderSuccessor(node_8)
    result_node_10 = findInorderSuccessor(node_10)
    result_node_14 = findInorderSuccessor(node_14)

    # Print results
    print(result_node_8.val if result_node_8 else None)
    print(result_node_10.val if result_node_10 else None)
    print(result_node_14.val if result_node_14 else None)
