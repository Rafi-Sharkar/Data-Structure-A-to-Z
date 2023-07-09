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
                cur = cur.next
            cur.next =  new_node 
    
    # display
    def display(self):
        cur = self.head
        while cur.next is not None:
            print(cur.data)
            cur = cur.next
        print(cur.data)
        
    # getAverage()
    def getAverage(self):
        sum = 0
        count = 0
        cur = self.head
        while cur.next is not None:
            sum += cur.data
            count += 1
            cur = cur.next
        sum += cur.data
        count += 1
        return float(sum/count)

lst = SLL()
lst.Add_last(5)
lst.Add_last(6)
lst.Add_last(7)
lst.Add_last(8)
lst.display()
print("average")
print(lst.getAverage())