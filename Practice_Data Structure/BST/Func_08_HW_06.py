class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
    
def calculate_sum(root):
    if root == None:
        return 0
    return calculate_sum(root.left) + calculate_sum(root.right) + root.data

root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

print(calculate_sum(root))