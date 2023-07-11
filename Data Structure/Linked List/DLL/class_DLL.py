class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def Add_last(self, value):
        new_node = Node(value)
        
    
    def display(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next


    def display_rev(self):
        cur = self.tail