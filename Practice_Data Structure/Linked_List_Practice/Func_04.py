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
    # Size
    def size(self):
        cur = self.head
        count = 0
        while cur.next is not None:
            count += 1
            cur = cur.next
        count += 1
        return count

    # addNodeBeforeValue
    def addNodeBeforeValue(self, givenValue, newValue):
        new_node = Node(newValue)
        if self.head.data == givenValue:
            new_node.next = self.head
            self.head = new_node
        else:
            cur = self.head
            while cur is not None:
                if cur.next is not None and cur.next.data == givenValue:
                    new_node.next = cur.next
                    cur.next = new_node
                    return
                else:
                    cur = cur.next
            if not cur:
                print("Given value is not found")
            



lst = SLL()
lst.Add_last(3)
lst.Add_last(6)
lst.Add_last(7)
lst.Add_last(10)
lst.display()
print()
lst.addNodeBeforeValue(3,2)
lst.display()