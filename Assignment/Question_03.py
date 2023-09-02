# Q4: Find the predecessor and successor of 10 in the following BST.

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
        self.numOfDescendants = 0

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        par = None
        cur = self.root
        while cur is not None:
            par = cur
            if value < cur.data:
                cur = cur.left
            else:
                cur = cur.right
        if value < par.data:
            par.left = Node(value)
        else:
            par.right = Node(value)
    
    def inOrder(self,cur):
        if cur is None:
            return
        self.inOrder(cur.left)
        print(cur.data, end=">")
        self.inOrder(cur.right)

    def countDescendants(self,cur):
        if cur is None:
            return 0 
        return (1 + self.countDescendants(cur.left) + self.countDescendants(cur.right))

bst = BST()
bst.insert(7)
bst.insert(4)
bst.insert(8)
bst.insert(3)
bst.insert(6)
bst.insert(5)
bst.inOrder(bst.root)
print()
print(bst.countDescendants(bst.root))


