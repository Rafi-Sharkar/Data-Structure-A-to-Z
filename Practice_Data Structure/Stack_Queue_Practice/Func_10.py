# Queue
class Queue:
    def __init__(self):     # create a queue 
        self.arr = []
    # enqueue
    def enqueue(self, value):
        return self.arr.append(value)
    # dequeue
    def dequeue(self):
        return self.arr.pop(0)
    # display
    def display(self):
        return self.arr
    # size
    def size(self):
        return len(self.arr)
    # isEmpty
    def isEmpty(self):
        return self.size()==0
    # peek
    def peek(self):
        return self.arr[0]
    
# Write code

class myStack():
    def __init__(self):
        self.Q1 = Queue()
        self.Q2= Queue()
    # enqueue
    def push(self, value):
        return self.Q1.enqueue(value)
    # dequeue
    def pop(self):
        if self.Q1.isEmpty():
            return "Stack is empty"
        while self.Q1.size() >=2:
            self.Q2.enqueue(self.Q1.dequeue())
        rm = self.Q1.dequeue()
        while self.Q2.size():
            self.Q1.enqueue(self.Q2.dequeue())        
        
    # size
    def sizeS(self):
        return self.Q1.size()
    #isEmpty
    def isEmptyS(self):
        return self.Q1.size() == 0
    #peek
    def peekS(self):
        if self.Q1.isEmpty():
            return "Stack is empty"
        while self.Q1.size()>1:
            self.Q2.enqueue(self.Q1.dequeue())
        rm = self.Q1.peek()
        while self.Q2.size():
            self.Q1.enqueue(self.Q2.dequeue())
        return rm
    #queuePrint
    def stackPrint(self):
        return self.Q1.display()
# write code

S = myStack()
S.push(13)
S.push(7)
S.push(25)
S.push(4)
S.push(11)
print(S.stackPrint())
print("\n")
S.pop()
print(S.stackPrint())
S.pop()
print(S.stackPrint())
S.pop()
print(S.stackPrint())

print(S.sizeS())
print(S.isEmptyS())
print(S.peekS())