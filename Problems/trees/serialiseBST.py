class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str

        use preorder traversal
        """
        if root is None: 
            return "#"

        return  f"{root.val},{self.serialize(root.left)},{self.serialize(root.right)}"


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(",")
        return self.helper(nodes)

    def helper(self,data):
        value = data.pop(0)

        if value == '#':
            return None

        node = TreeNode(int(value))
        node.left = self.helper(data)
        node.right = self.helper(data)

        return node
        
