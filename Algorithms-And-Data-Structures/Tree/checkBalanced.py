class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def is_balanced(root):
    """
    Check if a binary tree is balanced.
    A balanced tree is one where the heights of the two subtrees of any node
    never differ by more than one.
    
    :param root: TreeNode, the root of the binary tree
    :return: bool, True if the tree is balanced, False otherwise
    """
    if root is None: return True
    left_height = check_height(root.left)
    right_height = check_height(root.right)
    # recursively compute if subtrees are also balanced
    return abs(left_height - right_height) <= 1 and is_balanced(root.left) and is_balanced(root.right)


def check_height(root):
    if root is None:
        return 0
    return max(check_height(root.left), check_height(root.right)) + 1


def test_balanced():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    balanced = is_balanced(root)

    # should output "The tree is balanced."
    if balanced:
        print("The tree is balanced.")
    else:
        print("The tree is not balanced.")

def test_not_balanced():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.right = TreeNode(7)

    balanced = is_balanced(root)

    # should output "The tree is not balanced."
    if balanced:
        print("The tree is balanced.")
    else:
        print("The tree is not balanced.")
if __name__ == "__main__":
  test_balanced()
  test_not_balanced()