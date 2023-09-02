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
                print(cur.data,end="->")
                cur = cur.next
            print(cur.data)
    # Size
    def size(self):
        cur = self.head
        count = 0
        while cur.next is not None:
            count += 1
            cur = cur.next
        count += 1
        return count

    # remove even form the linked list
    def reverse(self):
        prev = None
        cur = self.head
        while cur is not None:
            t = cur.next
            cur.next = prev
            prev = cur
            cur = t
        self.head = prev
        


"""
how to write paper 
"""
                


lst = SLL()

lst.Add_last(1)

lst.Add_last(2)
lst.Add_last(3)

lst.Add_last(4)
lst.Add_last(5)

lst.display()
print()
lst.reverse()
print("after remove even ")
lst.display()

