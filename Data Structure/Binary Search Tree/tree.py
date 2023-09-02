class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, v):
        if self.root == None:
            self.root = Node(v)
            return   
    
        par = None
        cur = self.root
        while cur is not None:
            par = cur
            if v < cur.data:
                cur = cur.left
            else:
                cur = cur.right
        
        new_node = Node(v)
        if v< par.data:
            par.left = new_node
        else:
            par.right = new_node
        

    def find(self, v):
        cur = self.root
        while cur is not Node:
            if vur.data == v:
                return True
            if v<cur.data:
                cur = cur.left
            else:
                cur = cur.right
        return False

    def remove(self, v):
        if self.find(v) is False:
            return

        par = None
        cur = self.root
        while cur is not None:
            if cur.data == v :
                break
            par = cur
            if v < cur.data:
                cur = cur.left
            else:
                cur = cur.right

        # case_01-leaf node
        if cur.left is None and cur.right is None:        
            if cur.data < par.data:
                par.left = None
            else:
                par.right = None
        # case_02-one child
        elif (cur.left is None) != (cur.right is None):
            if cur.left is None:
                child = cur.right
            else:
                child = cur.left
            
            if cur.data < par.data:
                par.left = Child
            else:
                par.right = child
bst = BST()
for v in [20, 59, 66, 9, 34, 3, 28]:



# pre-order : 20, 9, 3, 59, 34, 28, 44, 58, 66, 73
# in-order : 3, 9, 20, 28, 34, 44, 58, 59, 66, 73
# post-order : 3, 9, 28, 58, 44, 34,73, 66, 59, 20





root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.left.left.left = Node('g')
root.left.left.right = Node('h')
root.right = Node('c')
root.right.left = Node('e')
root.right.left.left = Node('i')
root.right.right = Node('f')
root.right.right.left = Node('j')
root.right.right.right = Node('k')



def traverse(cur):
    if cur in None:   
        return                # if cur in Not None:   
    traverse(cur.left)
    traverse(cur.right)
    print(cur.data, end="->")

traverse(bst.root)


# remove type
# 1. leaf node
# 2. One child
# 3. Two child

