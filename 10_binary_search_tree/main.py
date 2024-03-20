#representation of a node in a binary search tree
class TreeNode:
   def __init__(self, key): 
       self.key = key
       self.left = None 
       self.right = None
       
#representation of the binary search tree
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        self.root = self._insert(self.root, key)
    
    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node
#search functionality
    def search(self, key):
        return self._search(self.root, key)
     
    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)
#deletion of nodes
    def delete(self, key):
        self.root = self._delete(self.root, key)
    
    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        #conditionals valid if there are 2 children
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            node.key = self._min_value(node.right)
            node.right = self._delete(node.right, key)
        return node
#chooses the smallest element from the right subtree and places it in place of the deleted node
    def _min_value(self, node):
        while node.left is not None:
            node = node.left
        return node.key