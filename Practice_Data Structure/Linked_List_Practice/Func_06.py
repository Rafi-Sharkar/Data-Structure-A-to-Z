class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
    
    # Add from last
    def Add_last(self, data):
        new_node = Node(data)
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

    # Sorted_insert
    def sorted_Insert(self,x):
        new_node=Node(x)
        cur = self.head
        while cur is not None:
            if cur.data > x:
                new_node.next = self.head
                self.head = new_node
                break
            elif cur.data < x and cur.next is not None and cur.next.data >= x:
                new_node.next = cur.next
                cur.next = new_node
                break
            elif cur.data < x and cur.next is None:
                cur.next = new_node
                break
            else:
                cur = cur.next


lst = SLL()
lst.Add_last(3)
lst.Add_last(5)
lst.Add_last(6)
lst.Add_last(7)
lst.Add_last(10)
lst.display()
print()
lst.sorted_Insert(7)
lst.display()