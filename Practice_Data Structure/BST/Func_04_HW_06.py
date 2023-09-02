class Node: 
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

# def numOfDescendants(root):
#     if root == None:
#         return 0
#     l = numOfDescendants(root.left)
#     r = numOfDescendants(root.right)
#     return l + r + 1

def count(cur):
    if cur == None:
        return 0
    c = 0 
    if cur.left != None:
        c += 1 
    if cur.right != None:
        c += 1
    return count(cur.left) + count(cur.right) + c

def printLevelOrder(root):
    if root == None:
        return
    queue = []
    queue.append(root)
    x = "A"
    while len(queue) > 0:
        print(f"{x} has { count(queue[0])} descendants")
        x = chr(ord(x)+1)
        node = queue.pop(0)
        if node.left != None:
            queue.append(node.left)
        if node.right != None:
            queue.append(node.right)





root = Node(7)
root.right = Node(8)
root.left = Node(4)
root.left.left = Node(3)
root.left.right = Node(6)
root.left.right.left = Node(5)

printLevelOrder(root)
