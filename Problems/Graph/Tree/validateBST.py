class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root):
    def is_valid(node, min_val=float('-inf'), max_val=float('inf')):
        if not node:
            return True
        
        if not (min_val < node.val < max_val):
            return False
        
        return (is_valid(node.left, min_val, node.val) and
                is_valid(node.right, node.val, max_val))
    
    return is_valid(root)

def testValidBST():
    # expected true
    root = TreeNode(1)
    root.left = TreeNode(-1)
    root.right = TreeNode(3)
    return isValidBST(root)

def testInvalidBST():
    # expected false
    root = TreeNode(6)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    return isValidBST(root)
    

""" O(n) time complexity """   
if __name__ == "__main__":
    print(testValidBST())
    print(testInvalidBST())

"""Example of misconstrued solution:

def isValidBST(root):
    # case 1: root is None
    if root is None: return True

    # case 2: root has no children
    if root.left is None and root.right is None: return True

    # case 3: root has only one child
    if root.left is None:
        return root.right.val > root.val and isValidBST(root.right)
    if root.left is None:
        return root.left.val < root.val and isValidBST(root.right)
    
    # case 4: both children exist
    return root.left.val < root.val and root.right.val > root.val and isValidBST(root.left) and isValidBST(root.right)

This solution fails to check every node on left subtree is guaranteed to be smaller than smallest value seen so far.

For example if fails to consider this counter example:

     0
    / \
   -1  2
   / \
  -2  3

  This solution will return True, but it is not a valid BST as 3 is on the left side of parent node 0 and should strictly be smaller.
"""