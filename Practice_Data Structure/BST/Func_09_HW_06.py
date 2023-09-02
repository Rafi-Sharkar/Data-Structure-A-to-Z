class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
    
def countNodes(root):
    if root == None:
        return 0
    return countNodes(root.left) + countNodes(root.right) + 1

root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

print(countNodes(root))