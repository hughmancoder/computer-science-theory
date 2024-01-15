class TreeNode:
    def __init__(self, val: int):
        self.value = val
        self.left = None
        self.right = None

def pathswithSum(node: TreeNode, target: int) -> int:

    def helper(node: TreeNode, runningSum: int):
        if node is None:
            return 0
        
        leftCount = helper(node.left, runningSum - node.value)
        rightCount = helper(node.right, runningSum - node.value)
        
        if runningSum - node.value == 0:
            return 1 + leftCount + rightCount
        else: 
            return leftCount + rightCount
        
    return helper(node, target)


"""Example test case:
     0
    / \
   1    2
  / \   / \
 -1  3  4 -2
"""

if __name__ == "__main__":
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.left.left = TreeNode(-1)
    root.left.right = TreeNode(3)

    root.right = TreeNode(2)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(-2)

    print(pathswithSum(root, 0), 3) 
    print(pathswithSum(root, 6), 1) 
    


