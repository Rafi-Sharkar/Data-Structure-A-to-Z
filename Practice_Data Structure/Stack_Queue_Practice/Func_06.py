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

# write code
    
Q = Queue()
Q.enqueue(10)
Q.enqueue(20)
Q.enqueue(30)
Q.enqueue(40)
Q.enqueue(50)
Q.enqueue(60)
Q.enqueue(70)
Q.enqueue(80)
Q.enqueue(90)
print(Q.display())

# input

k = int(input("Reverse the first 'k' ekements of a queue. K = "))
for i in range(k):
    Q.enqueue(Q.dequeue())
print(Q.display())

    