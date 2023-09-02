class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    # Display
    def display(self):
        cur = self.head
        if cur is None:
            print("Linked List is Empty")
        else:
            while cur is not None:
                print(cur.data)
                cur = cur.next

    # Add element at last
    def Addlast(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node
        
    # Add element at first
    def Addfirst(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
    # Add element after the tergated value
    def Add_after_X(self, x, value):
        new_node = Node(value)
        cur = self.head
        while cur is not None:
            if cur.data == x:
                new_node.next = cur.next
                cur.next = new_node
                break
            else:
                cur = cur.next

    # Add element before the tergated value
    def Add_before_X(self, x, value):
        new_node = Node(value)
        cur = self.head
        while cur is not None:
            if cur.next.data == x:
                new_node.next = cur.next
                cur.next = new_node
                break                
            else:
                cur = cur.next
            
    # Remove element form last
    def remove_last(self):
        cur = self.head
        while cur.next.next is not None:
            cur = cur.next
        cur.next = None
    
    # Remove element form first
    def remove_first(self):
        cur = self.head
        self.head = cur.next

    
    # Remove element after the tergated value
    def remove_after_x(self, x):
        cur = self.head
        while cur is not None:
            if cur.data == x:
                cur.next = cur.next.next
                break
            else:
                cur = cur.next

    # Remove element before the tergated value
    def remove_before_x(self, x):
        cur = self.head
        while cur is not None:
            if cur.next.next.data == x:
                cur.next = cur.next.next
                break
            else:
                cur = cur.next

    # Search
    def Search(self, x):
        cur = self.head
        while cur is not None:
            if cur.data == x:
                print(f"{x} is exist in Linked List")
                break
            else:
                cur = cur.next

        

    

lst = SLL()
lst.Addlast(6)
lst.Addlast(9)
lst.Addlast(11)
lst.Addlast(14)
lst.Addlast(17)
lst.Search(6)
lst.display()
print()


# lst.Add_after_X(11,13)
# lst.display()
    