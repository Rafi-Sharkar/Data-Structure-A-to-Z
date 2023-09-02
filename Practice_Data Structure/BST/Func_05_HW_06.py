class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
    
def pre_Order(root, sol):
    if root == None:
        return
    sol.append(root.data)
    pre_Order(root.left, sol)
    pre_Order(root.right, sol)

def in_Order(root, sol):
    if root == None:
        return
    in_Order(root.left, sol)
    sol.append(root.data)
    in_Order(root.right, sol)

def post_Order(root, sol):
    if root == None:
        return
    post_Order(root.left, sol)
    post_Order(root.right, sol)
    sol.append(root.data)

def Is_Identical(root_01, root_02):
    arr_01 = []
    arr_02 = []

    # check pre_Order is same
    pre_Order(root_01, arr_01)
    pre_Order(root_02, arr_02)
    if arr_01 != arr_02:
        return False
    # Clear array
    arr_01.clear()
    arr_02.clear()

    # check in_Order is same
    in_Order(root_01, arr_01)
    in_Order(root_02, arr_02)
    if arr_01 != arr_02:
        return False
    # Clear array
    arr_01.clear()
    arr_02.clear()

    # check post_Order is same
    post_Order(root_01, arr_01)
    post_Order(root_02, arr_02)
    if arr_01 != arr_02:
        return False
    # Clear array
    arr_01.clear()
    arr_02.clear()

    return True


root1 = Node(5)
root1.left = Node(3)
root1.right = Node(8)
root1.left.left = Node(2)
root1.left.right = Node(4)

root2 = Node(5)
root2.left = Node(3)
root2.right = Node(8)
root2.left.left = Node(2)
root2.left.right = Node(4)
root2.left.left.left = Node(1)

print(Is_Identical(root1, root2))
