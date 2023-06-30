# SLL

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def display(self):
        cur = self.head
        print("Head",end=">")
        while cur is not None:
            print(cur.data, end=">")
            cur = cur.next

    def find(self, v):
        cur = self.head
        while cur is not None:
            if cur.data == v:
                return True
            cur = cur.next
        return False

    def append(self, v):
        new_node = Node(v)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node


# write code

sll = SLL()
sll.append("f")
sll.append("h")
sll.append("g")
sll.append("h")
sll.append("i")
sll.display()
