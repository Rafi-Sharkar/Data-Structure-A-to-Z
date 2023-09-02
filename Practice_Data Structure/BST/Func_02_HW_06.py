# largest element in each level of a BST

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
    
def height(root):
    if root == None:
        return 0
    return max(height(root.left), height(root.right)) + 1

def level_order_print(root):
    for i in range(1, height(root)+1):
        arr = []
        print_cur_level(root, i, arr)
        print(f"largest element in level {i} is {max(arr)}")


def print_cur_level(root, level, arr = []):
    if root == None:
        return
    if level == 1:
        # print(root.data, end=" ")
        arr.append(root.data)
    elif level > 1: 
        print_cur_level(root.left, level-1, arr)
        print_cur_level(root.right, level-1, arr)




root = Node(10)
root.left = Node(5)
root.right = Node(13)
# root.right.left = Node(11)
# root.right.right = Node(14)
root.left.left = Node(3)
root.left.right = Node(7)

print(f"Height of the BST is {height(root)}")
level_order_print(root)