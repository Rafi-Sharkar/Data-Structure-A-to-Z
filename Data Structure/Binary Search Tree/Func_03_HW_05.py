import random
class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def helperinsertR(value, cur, par):
    if cur == None:
        if value < par.data:
            par.left = Node(value)
            return
        else:
            par.right = Node(value)
            return
    par = cur
    if value < cur.data:
        helperinsertR(value, cur.left, par)
    else:
        helperinsertR(value, cur.right, par)

class BST:
    def __init__(self):
        self.root = None

    # insert recursion
    def insertR(self,value):
        if(self.root==None):
            self.root=Node(value)
            return
        helperinsertR(value, self.root, None)        

    # inOrder
    def inOrder(self,cur):
        if cur == None:
            return
        self.inOrder(cur.left)
        print(cur.data, end="->")
        self.inOrder(cur.right)
    
    # findMaxR
    def findMaxR(self, root):
        if root is None:
            print("BST is empty")
            return
        if root.right is None:
            print("Max: ",root.data)
            return
        self.findMaxR(root.right)


lst = [42, 52, 23, 22, 24, 56, 32, 62, 53, 11, 27, 28]
# for i in range(1,13):
#     lst.append(random.randint(10,70))
# print(lst)

bst = BST()
for i in lst:
    bst.insertR(i)
bst.inOrder(bst.root)
bst.findMaxR(bst.root)
