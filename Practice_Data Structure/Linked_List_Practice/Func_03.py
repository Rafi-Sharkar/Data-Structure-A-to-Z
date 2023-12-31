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

lst1 = SLL() 
lst2 = SLL()
lst3 = SLL()

# equalNode
def equalNode(lst_A, lst_B):
    equal = True
    if lst_A.size() != lst_B.size():
        equal = False
    else:
        cur_A = lst_A.head
        cur_B = lst_B.head
        while cur_A.next is not None:
            if cur_A.data == cur_B.data:
                cur_A = cur_A.next
                cur_B = cur_B.next
            else:
                equal = False
                break
    if equal == True:
        print(f"A and B are same!!")
    else:
        print(f"A and B aren't same!!")
# linked list_1
lst1.Add_last(7)  
lst1.Add_last(6)  
lst1.Add_last(10)  
lst1.Add_last(11)  

# linked lsit_2
lst2.Add_last(7)  
lst2.Add_last(16)  
lst2.Add_last(10)  
lst2.Add_last(11) 

# linked lsit_2
lst3.Add_last(7)  
lst3.Add_last(6)  
lst3.Add_last(10)  
  
equalNode(lst2, lst3)
# print(lst3.size())
  

