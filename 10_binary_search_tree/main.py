#representation of a node in a binary search tree
class TreeNode:
   def __init__(self, key): 
       self.key = key
       self.left = None 
       self.right = None
       
#representation of a binary search tree
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        self.root = self._insert(self.root, key)
    
    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)