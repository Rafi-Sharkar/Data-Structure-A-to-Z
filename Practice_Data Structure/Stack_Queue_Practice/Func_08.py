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
