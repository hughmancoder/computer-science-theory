import random

class TreeNode: 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.size = 1

    def insert_in_order(self, value):
        if value <= self.data:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert_in_order(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert_in_order(value)
        self.size += 1

    def get_random_node(self):
        left_size = self.left.size if self.left else 0
        index = random.randint(0, self.size - 1)
        if index < left_size:
            return self.left.get_random_node()
        elif index == left_size:
            return self
        else:
            return self.right.get_random_node()

    def find(self, value):
        if value == self.data:
            return self
        elif value < self.data:
            return self.left.find(value) if self.left else None
        else:
            return self.right.find(value) if self.right else None

    def size(self):
        return self.size


class Tree:
    def __init__(self):
        self.root = None

    def insert_in_order(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self.root.insert_in_order(value)

    def get_random_node(self):
        if self.root is None:
            return None
        else:
            return self.root.get_random_node()


class Tests:
    def assert_equal(self, output, expected):
        print(f"Output: {output}, Expected: {expected}")
        assert output == expected

    def test_empty_tree(self):
        tree = Tree()
        self.assert_equal(tree.get_random_node(), None)
        self.assert_equal(tree.root, None)

    def test_insertion_and_size(self):
        tree = Tree()
        tree.insert_in_order(5)
        self.assert_equal(tree.root.data, 5)
        self.assert_equal(tree.root.size, 1)

        tree.insert_in_order(3)
        tree.insert_in_order(7)
        self.assert_equal(tree.root.size, 3)

   

    def test_random_node_retrieval(self):
        tree = Tree()
        tree.insert_in_order(5)
        tree.insert_in_order(-1)
        tree.insert_in_order(2)
        tree.insert_in_order(102)
        tree.insert_in_order(7)

        random_node = tree.get_random_node()
        print("Random node", random_node.data)

        

# To run the tests
if __name__ == "__main__":
    tests = Tests()
    tests.test_empty_tree()
    tests.test_insertion_and_size()
    tests.test_random_node_retrieval()



"""
APPENDIX:

Delete cases

1) Delete node with zero children

  0
 /  \ 
-1   2

delete(TreeNode(-1)
self.node = None

2) Delete node with one child

  0
   \ 
    2


Delete(TreeNode(0))

if parent.left is not None:
    parent.value = parent.left.value
    temp = parent.left
    parent.left = temp.left
    parent.right = temp.right

likewise for parent.right


3) Delete node with two children

  0
 /  \ 
-1   2

Delete(TreeNode(0))

- next largest node becomes treeNode (inorder successor: smallest node in right subtree)

successor = getInorderSuccessor(TreeNode(0))
node.left = tempLeft
node.right = tempRight
node.value = successor.value
successor = None
successor.right = tempRight
successor.left = tempLeft


"""