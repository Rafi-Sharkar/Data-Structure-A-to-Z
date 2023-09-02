# Iterative using queue
# Method_01
# '''
class Node:
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None

def printLevelOrder(root):
	if root is None:
		return
	queue = []
	queue.append(root)
	while(len(queue) > 0):
		print(queue[0].data, end=" ")
		node = queue.pop(0)

		if node.left is not None:
			queue.append(node.left)

		if node.right is not None:
			queue.append(node.right)

# Driver Program to test above function
root = Node(10)
root.left = Node(5)
root.right = Node(13)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.right = Node(14)

print("Level Order Traversal of binary tree is -")
printLevelOrder(root)
# '''

# Recursive way
# Method_02
'''
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def height(root):
    if (root == None):
        return 0 
    return max(height(root.left), height(root.right)) + 1

def print_cur_level(root, level):
    if root == None:        # Base case
        return
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        print_cur_level(root.left, level-1)
        print_cur_level(root.right, level-1)

def level_order_Print(root):
    for i in range(1, height(root)+1):
        print_cur_level(root, i)
        print()

root = Node(10)
root.left = Node(5)
root.right = Node(13)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.right = Node(14)
print(f"Height of the tree: {height(root)}")
level_order_Print(root)
'''
