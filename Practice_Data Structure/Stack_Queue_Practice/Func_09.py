# Stack
class stack:
    def __init__(self):     # initializing the stack
        self.arr = []
    #push
    def push(self, value):
        return self.arr.append(value)
    #pop
    def pop(self):
        if self.isEmpty():
            return "Srack is empty"
        return self.arr.pop()
    #lenght
    def size(self):
        return len(self.arr)
    #isEmpty
    def isEmpty(self):
        return self.size() == 0
    #peek
    def peek(self):
        if self.isEmpty():
            return "Stake is empty"
        return self.arr[-1]
    #stack print
    def stackPrint(self):
        return self.arr
    
# Write code

class myQueue():
    def __init__(self):
        self.stk1 = stack()
        self.stk2= stack()
    # enqueue
    def enqueue(self, value):
        return self.stk1.push(value)
    # dequeue
    def dequeue(self):
        if self.stk1.isEmpty():
            return "Queue is empty"
        while self.stk1.size()>1:
            self.stk2.push(self.stk1.pop())
        rm = self.stk1.pop()
        while self.stk2.size():
            self.stk1.push(self.stk2.pop())
        # return rm
        
    # size
    def sizeq(self):
        return self.stk1.size()
    #isEmpty
    def isEmptyq(self):
        return self.stk1.size() == 0
    #peek
    def peekq(self):
        if self.stk1.isEmpty():
            return "Queue is empty"
        while self.stk1.size()>1:
            self.stk2.push(self.stk1.pop())
        rm = self.stk1.peek()
        while self.stk2.size():
            self.stk1.push(self.stk2.pop())
        return rm
    #queuePrint
    def queuePrint(self):
        return self.stk1.stackPrint()
# write code

Q = myQueue()
Q.enqueue(13)
Q.enqueue(7)
Q.enqueue(25)
Q.enqueue(4)
Q.enqueue(11)
print(Q.queuePrint())
print("\n")
Q.dequeue()
print(Q.queuePrint())
Q.dequeue()
print(Q.queuePrint())
Q.dequeue()
print(Q.queuePrint())

print(Q.sizeq())
print(Q.isEmptyq())
print(Q.peekq())