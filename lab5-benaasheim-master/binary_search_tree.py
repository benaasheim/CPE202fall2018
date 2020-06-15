
from queue_array import Queue

class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right
    def _search(self, key):
        if self.key > key:
            if self.left != None:
                return self.left._search(key)
            else:
                return False
        elif self.key < key:
            if self.right != None:
                return self.right._search(key)
            else:
                return False
        else:
            return self.data
    def _insert(self, key, data):
        if self.key > key:
            if self.left == None:
                self.left = TreeNode(key, data)
            else:
                self.left._insert(key, data)
        elif self.key < key:
            if self.right == None:
                self.right = TreeNode(key, data)
            else:
                self.right._insert(key, data)
        else:
            self.data = data
    def _find_min(self):
        if self.left == None:
            return (self.key, self.data)
        else:
            return self.left._find_min()
    def _find_max(self):
        if self.right == None:
            return (self.key, self.data)
        else:
            return self.right._find_max()
    def _height(self, count):
        print(self.key, count)
        if self.right == None:
            if self.left == None:
                return count
            else:
                left = self.left._height(count+1)
                return left
        else:
            if self.left == None:
                right = self.right._height(count+1)
                return right
            else:
                left = self.left._height(count+1)
                right = self.right._height(count+1)
                if right > left:
                    return right
                else:
                    return left
    def LNR(self):
        if self.left == None:
            if self.right == None:
                return [self.key]
            else:
                return [self.key] + self.right.LNR()
        else:
            if self.right == None:
                return self.left.LNR() + [self.key]
            else:
                return self.left.LNR() + [self.key] + self.right.LNR()
    def NLR(self):
        if self.left == None:
            if self.right == None:
                return [self.key]
            else:
                return [self.key] + self.right.NLR()
        else:
            if self.right == None:
                return [self.key] + self.left.NLR()
            else:
                return [self.key] + self.left.NLR() + self.right.NLR()
    #def lol(self, q):
    #    if self.left != None:
    #        q.enqueue(self.left.key)
    #        if self.right != None:
    #            q.enqueue(self.right.key)
    #        self.left.lol(q)
    #        if self.right != None:
    #            self.right.lol(q)
    #    else:
    #        if self.right != None:
    #            q.enqueue(self.right.key)
    #        if self.right != None:
    #            self.right.lol(q)
    #            
        
class BinarySearchTree:

    def __init__(self): # Returns empty BST
        self.root = None

    def is_empty(self): # returns True if tree is empty, else False
        return self.root == None

    def search(self, key): # returns True if key is in a node of the tree, else False
        if self.root == None:
            return False
        else:
            return self.root._search(key)

    def insert(self, key, data=None): # inserts new node w/ key and data
        # If an item with the given key is already in the BST, 
        # the data in the tree will be replaced with the new data
        # Example creation of node: temp = TreeNode(key, data)
        if self.root == None:
            self.root = TreeNode(key, data)
        else:
            self.root._insert(key, data)

    def find_min(self): # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        if self.root == None:
            return None
        else:
            return self.root._find_min()

    def find_max(self): # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        if self.root == None:
            return None
        else:
            return self.root._find_max()

    def tree_height(self): # return the height of the tree
        # returns None if tree is empty
        if self.root == None:
            return None
        else:
            return self.root._height(0)

    def inorder_list(self): # return Python list of BST keys representing in-order traversal of BST
        if self.root == None:
            return []
        else:
            return self.root.LNR()

    def preorder_list(self):  # return Python list of BST keys representing pre-order traversal of BST
        if self.root == None:
            return []
        else:
            return self.root.NLR()
    def level_order_list(self):  # return Python list of BST keys representing level-order traversal of BST
        # You MUST use your queue_array data structure from lab 3 to implement this method
        q = Queue(25000) # Don't change this!
        if self.root == None:
            return []
        else:
            q.enqueue(self.root)
            x = []
            while q.num_items > 0:
                cur = q.dequeue()
                x += [cur.key]
                if cur.left != None:
                    q.enqueue(cur.left)
                if cur.right != None:
                    q.enqueue(cur.right)
            #self.root.lol(q)
            #print(q.items[:5])
            #x = []
            #for i in range(q.num_items):
            #    x += [q.dequeue()]
            return x
