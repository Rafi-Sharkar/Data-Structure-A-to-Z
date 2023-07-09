class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, v):
        new_node = Node(v)
        if self.head is None:
            self.head = new_node
        else:
            # self.tail.next = new_node
            cur = self.head
            while cur is not None:
                if cur.next is None:
                    break
                cur = cur.next
        self.tail = new_node
        self.size += 1

    def appendLeft(self, v):
        new_node = Node(v)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self.size += 1

    def popleft(self):
        if self.head is None:
            raise IndexError("pop from empty list")
        v =self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return v

    def pop(self):
        cur = self.head
        while cur is not None:
            if cur.next.next is None:
                break
            cur = cur.next

        cur.next = None
        self.tail = cur

    def remove(self, v):
        if self.head is None:
            raise IndexError("remove from empty list")
        if self.head.data == v:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.size -= 1
            return
        cur = self.head
        while cur is not None:
            if cur.next.data == v:
                break
            cur = cur.next
        if cur is None:
            raise ValueError("SLL.remove(x): x not in SLL")
        cur.next = cur.next.next
        if cur.next is None:
            self.tail = cur
        self.size -= 1
        

    def display(self):
        print("head", end="->")
        cur = self.head
        while cur is not None:
            print(f"{self.data}",end="->")
            cur = cur.next
        print("None")

    def find(self, v):
        cur = self.head
        while cur is not None:
            if cur.data == v:
                return True
            cur = cur.next
        return False

    def count(self, v):
        c = 0
        cur = self.head
        while cur is not None:
            if cur.data == v:
                c +=1
            cur = cur.next
        return c

    def sum(self):
        s = 0
        cur = self.head
        while cur is not None:
            s += cur.data
            cur = cur.next
        return c
    
    def average(self):
        s = 0
        n = 0
        cur = self.head
        while cur is not None:
            s += cur.data
            n += 1
            cur = cur.next
        return s/n
    




'''
1. Check if list is empty
2. check if value is at head
3. loop and find the desired node
   3a. if not found
   3b. if found
'''