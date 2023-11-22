class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class MinimalTree:

    @staticmethod
    def CreateMinimalTree(numbers: list):
        return MinimalTree.helper(numbers, 0, len(numbers))

    @staticmethod
    def helper(numbers: list, l: int, r: int):
        if l >= r:
            return None
        m = (l + r) // 2
        node = TreeNode(numbers[m])
        node.left = MinimalTree.helper(numbers, l, m)
        node.right = MinimalTree.helper(numbers, m + 1, r)
        return node


numbers = [1, 2, 3, 4, 5, 6, 7]
tree_root = MinimalTree.CreateMinimalTree(numbers)
print(tree_root.data)