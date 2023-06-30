# Queue
class queue:
    def __init__(self):     # initialize queue
        self.arr = []
    #enqueue
    def enqueue(self, value):
        return self.arr.append(value)
    #dequeue
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.arr.pop(0)
    #size
    def size(self):
        return len(self.arr)
    #isEmpty
    def isEmpty(self):
        return self.size() == 0
    #peek
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"        
        return self.arr[0]
    #queuePrint
    def queuePrint(self):
        return self.arr

# write code

Q = queue()
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
print(Q.size())
print(Q.isEmpty())
print(Q.peek())
