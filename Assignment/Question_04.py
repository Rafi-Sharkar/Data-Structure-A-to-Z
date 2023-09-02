# Q4: Find the predecessor and successor of 10 in the following BST.

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

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

    # def find_Suc(self, value):
        # cur = self.root
        # if self.root is None:
        #     print(f"{value} is not found")
        # while cur is not None:
        #     if value == cur.data:
        #         break
        #     if value < cur.data:
        #         cur = cur.left
        #     else:
        #         cur = cur.right

        # par_S = cur
        # par_P = cur
        # suc = cur.right
        # pre = cur.left
        # while suc.left is not None:
        #     par_S = suc
        #     suc = suc.left
        # while pre.right is not None:
        #     par_P = pre
        #     pre = pre.right
        # self.lowest_value(cur, cur.right)
        # self.highest_value(cur, cur.left)


        # print(self.predecessor(cur).data)
        # print(self.successor(cur).data)

        
        # print(f"The predecessor of {value} is {self.predecessor(value).data} and the successor is {self.successor(value).data}.")

    # def successor(self, cur):
    #     if cur.right is None:
    #         return cur
    #     return self.lowest_value(cur, cur.right)

    # def predecessor(self, cur):
    #     if cur.left is None:
    #         return cur
    #     return self.highest_value(cur, cur.left)

    # def lowest_value(self, par, suc):
    #     if suc.left is None:
    #         return suc
    #     par = suc
    #     suc = suc.left
    #     self.lowest_value(par, suc)

    # def highest_value(self, par, suc):
    #     if suc.right is None:
    #         return suc
    #     par = suc
    #     suc = suc.right
    #     self.highest_value(par, suc)
        
    


def findPreSuc(root, value):
# Base Case
    if root is None:
        return
    # If key is present at root
    if root.data == value:
        # the maximum value in left subtree is predecessor
        if root.left is not None:
            tmp = root.leftre
            while(tmp.right):
                tmp = tmp.right
            findPreSuc.pre = tmp


        # the minimum value in right subtree is successor
        if root.right is not None:
            tmp = root.right
            while(tmp.left):
                tmp = tmp.left
            findPreSuc.suc = tmp

        return

    # If key is smaller than root's key, go to left subtree
    if root.data > value :
        findPreSuc.suc = root
        findPreSuc(root.left, value)

    else: # go to right subtree
        findPreSuc.pre = root
        findPreSuc(root.right, value)

bst = BST()
bst.insert(10)
bst.insert(5)
bst.insert(13)
bst.insert(14)
bst.insert(3)
bst.insert(7)
bst.inOrder(bst.root)
print()
# bst.find_Suc(3)
findPreSuc.pre = None
findPreSuc.suc = None
findPreSuc(bst.root, 10)


