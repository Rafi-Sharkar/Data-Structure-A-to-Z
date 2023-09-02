class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def Is_BST_Ruc(root):
    if root == None:
        return
    if root.left:
        if root.left.data > root.data:
            return False
    if root.right:
        if root.right.data < root.data:
            return False
    Is_BST_Ruc(root.left)
    Is_BST_Ruc(root.right)
    return True

def Is_BST_Ite(root):
    if root == None:
        print("BST is empty !!")
    while root != None:
        if root.left:
            if root.left.data > root.data:
                return False
            else:
                root = root.left
        if root.right:
            if root.right.data < root.data:
                return False
            else:
                root = root.right
    return True


root = Node(20)
root.left = Node(8)
root.right = Node(29)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

print(Is_BST_Ruc(root))
# print(Is_BST_Ite(root))
