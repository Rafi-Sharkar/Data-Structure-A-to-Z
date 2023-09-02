import random
class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        
    # insert iteration
    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
            return
        par = None
        cur = self.root
        while cur != None:
            par = cur
            if value < cur.data:
                cur = cur.left
            else:
                cur = cur.right
        if value < par.data:
            par.left = Node(value)
        else:
            par.right = Node(value)

    # inOrder
    def inOrder(self,cur):
        if cur == None:
            return
        self.inOrder(cur.left)
        print(cur.data, end="->")
        self.inOrder(cur.right)

lst = []
for i in range(1,13):
    lst.append(random.randint(10,70))
print(lst)

bst = BST()
for i in lst:
    bst.insert(i)
bst.inOrder(bst.root)