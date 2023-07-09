class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
    
    # Add from last
    def Add_last(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next is not None:
                cur  = cur.next
            cur.next = new_node

    # Display
    def display(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            cur = self.head
            while cur.next is not None:
                print(cur.data)
                cur = cur.next
            print(cur.data)

    # numOfOccurrences of x
    def numOfOccurrences(self, x):
        cur = self.head
        count = 0
        while cur.next is not None:
            if cur.data == x:
                count += 1
            cur = cur.next
        return f"{x} has {count} occerrence"



lst = SLL()
lst.Add_last(4)
lst.Add_last(7)
lst.Add_last(2)
lst.Add_last(4)
lst.Add_last(5)
lst.Add_last(4)
lst.Add_last(2)
lst.display()
print()
print(lst.numOfOccurrences(4))