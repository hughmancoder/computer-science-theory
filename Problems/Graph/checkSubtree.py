class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    
def isSubtree(T1: TreeNode, T2: TreeNode):
    def helper(node: TreeNode):
        if not node:
            return "X"
        """Case for delimiter:  
        For example, consider two trees: one with a root node of value 12 and another with a root of 1 having a left child with value 2. 
        Without delimiters, both trees could be serialized to the same string representation ("12 X X" or "1 2 X X X"), 
        """
        return f"#{node.value} {helper(node.left)} {helper(node.right)}"
    structure_1 = helper(T1)
    structure_2 = helper(T2)
    return structure_2 in structure_1 



def test_isSubtree():
    # Test Case 1: T2 is a subtree of T1
    T1 = TreeNode(1)
    T1.left = TreeNode(2)
    T1.right = TreeNode(3)
    T1.left.left = TreeNode(4)
    T1.left.right = TreeNode(5)

    T2 = TreeNode(2)
    T2.left = TreeNode(4)
    T2.right = TreeNode(5)

    assert isSubtree(T1, T2) == True, "Test Case 1 Failed"

    # Test Case 2: T2 is not a subtree of T1
    T3 = TreeNode(6)
    assert isSubtree(T1, T3) == False, "Test Case 2 Failed"

    # Test Case 3: T2 is identical to T1
    T4 = TreeNode(1)
    T4.left = TreeNode(2)
    T4.right = TreeNode(3)
    T4.left.left = TreeNode(4)
    T4.left.right = TreeNode(5)

    assert isSubtree(T1, T4) == True, "Test Case 3 Failed"

    # Test Case 4: T2 is a subtree but not from the root
    T5 = TreeNode(3)
    assert isSubtree(T1, T5) == True, "Test Case 4 Failed"

    print("All test cases passed!")

# Run the tests
test_isSubtree()
