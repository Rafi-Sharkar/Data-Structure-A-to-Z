class Node:
    def __init__(self,value):
        self.data=value
        self.prev=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None

    def append(self,value):
        newNode=Node(value)
        if(self.head==None):
            self.head=newNode
        else:
            cur=self.head
            while cur!=None:
                if(cur.next==None):
                    cur.next=newNode
                    newNode.prev=cur
                    break
                else:
                    cur=cur.next

    def appendleft(self,value):
        newNode=Node(value)
        if(self.head==None):
            self.head=newNode
        else:
            newNode.next=self.head
            self.head.prev=newNode
            self.head=newNode
    def append_after_x(self, x, value):
        new_node = Node(value)
        cur = self.head
        while cur is not None:
            if cur.data == x:
                new_node.prev = cur
                new_node.next = cur.next
                cur.next = new_node
                break
            else:
                cur = cur.next

    def Add_before_x(self, x, value):
        new_node = Node(value)
        cur = self.head
        if self.head.data == x:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            while cur is not None:
                if cur.data == x:
                    new_node.next = cur
                    new_node.prev = cur.prev
                    cur.prev.next = new_node
                    cur.prev = new_node
                    break
                else:
                    cur = cur.next

    def remove_right(self):
        cur = self.head
        while cur is not None:
            if cur.next is None:
                cur.prev.next = None
                break
            else:
                cur = cur.next                
    def remove_left(self):
        if(self.head==None):
            print("list is empty")
        else:
            t = self.head.next
            self.head.next.prev=None
            self.head=t
    def spasific_number(self,value):
        if(self.head.data==value):
            self.remove_left()
        else:
            cur=self.head
            while cur!=0:
                if(cur.data==value and cur.next==None):
                    self.remove_right()
                    break
                elif(cur.data==value):
                    cur.prev.next=cur.next
                    break
                else:
                    cur=cur.next

    def printdll(self):
        cur=self.head
        print("Head",end=" <-> ")
        while cur.next!=None:
            print(cur.data,end=" <-> ")
            cur=cur.next
        print(cur.data,end=" <-> None ")
s=dll()
s.append(5)
s.append(9)
s.append(4)
s.append(7)
s.appendleft(90)
s.appendleft(50)
s.appendleft(70)
s.spasific_number(9)
s.printdll()

