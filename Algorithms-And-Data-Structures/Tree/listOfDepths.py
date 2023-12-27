from collections import deque;

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def list_of_depths(root):
    """
    Creates a list of linked lists, where each linked list contains
    nodes at the same depth in the binary tree.
    :param root: TreeNode, the root of the binary tree
    :return: List of LinkedListNode, each representing a depth level
    """
    res = []
    node_map = {}
    q = deque([root])
    while q:
        levelSize = len(q)
        linkedListNode = LinkedListNode(None)
        linkedListRoot = linkedListNode
        for i in range(levelSize):
            treeNode = q.popleft()
            linkedListNode.next = LinkedListNode(treeNode.value)
            linkedListNode = linkedListNode.next

            if treeNode.left:
                q.append(treeNode.left)
            if treeNode.right:
                q.append(treeNode.right)
            
        # add level linked list to res
        res.append(linkedListRoot.next)
        
    return res

    

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    # Use list_of_depths() to get the depth lists
    depth_lists = list_of_depths(root)

    # Print the depth lists
    for i, linked_list in enumerate(depth_lists):
        print(f"Depth {i}: ", end="")
        current = linked_list
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
    
