class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def weaveLists(first, second, prefix, results):
    pass

def allSequences(node):
    pass

def BSTSequences(root):
    # TODO
    pass
       

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print(allSequences(root))

"""
Let's start with an example.

    4
   / \
  2   5 
 / \   \
1   3   6
To construct this tree we must insert the node 4 first. This node is always going to be the first element in each of the possible solution. Lets remove this node from the tree.

  2    5    
 / \    \
1   3    6
To continue construcing the tree from the example we now have a choice of eather inserting 2 or 5. Notice that both are the roots of the respective subtrees. Lets start with node 2 and remove it from the tree.

1   3   5
         \
          6

Algorithm:
          
start with a root of the tree (the only valid choice)

for each of the current valid choices:
- remove one of the roots (valid choices), add its children to the set of choices
- recursively find all possible solutions for the new set of choices
- append the root to the head of each of those solutions

the recursion ends when there are no remaining nodes (choices) left

"""
