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

    def remove(self,v):
        if self.head is None:
            raise IndexError("remove from empty list")
        if self.head.data == v:
            self.head = self.head.next
        
        cur = self.head
        while cur is not None:
            if cur.next is not None and cur.next.data == v:
                break
            cur = cur.next
        if cur is None:
            raise ValueError(f"{v} not in list")
        else:
            cur.next = xur.next.next
            if cur.next is None:
                suel.tail


    # remove even form the linked list
    def deleteeven(self):
        cur = self.head
        if cur.data%2==0:temp = cur.next;cur.next = None;self.head = temp;cur = self.head      
        while cur is not None:
            if cur.next is not None and cur.next.data%2==0:temp = cur.next.next;cur.next.next = None;cur.next = temp
            else:cur = cur.next
                


lst = SLL()
lst.Add_last(2)
lst.Add_last(3)
lst.Add_last(10)
lst.Add_last(16)
lst.Add_last(61)
lst.Add_last(108)
lst.display()
print()
lst.deleteeven()
print("after remove even ")
lst.display()
