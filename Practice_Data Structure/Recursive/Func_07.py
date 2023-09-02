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
            
    # Delete first k'th node in linked list
    def rec_delete(self, cur, k):
        if(self.head.data==k):
            self.head=self.head.next
            return

        if cur.next.data == k:
            cur.next = cur.next.next
            return
        return self.rec_delete(cur.next, k)


sll = SLL()
sll.Add_last(3)
sll.Add_last(2)
sll.Add_last(3)
sll.Add_last(7)
sll.Add_last(0)
sll.Add_last(1)
sll.display()
sll.rec_delete(sll.head, 3)
sll.display()