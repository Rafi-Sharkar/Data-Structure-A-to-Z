# check whether the leaf nodes of a BST is even or odd

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def leaf_nodes_check(root, arr = []):
    if root == None:
        return 
    if root.left == None and root.right == None:
        if root.data%2 == 0:
            print(f"{root.data} Even")
            arr.append("Even")
        else:
            print(f"{root.data} Odd")
            arr.append("Odd")

    leaf_nodes_check(root.left, arr)
    leaf_nodes_check(root.right, arr)

root = Node(10)
root.left = Node(5)
root.right = Node(13)
root.left.left = Node(3)
root.left.right = Node(7)
root.left.left = Node(1)     

arr = []
leaf_nodes_check(root, arr)
print(arr)