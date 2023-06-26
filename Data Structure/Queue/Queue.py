class queue():
    def __init__(self):
        self.arr = []

    def enqueue(self,v):
        self.arr.append(v)
    
    def dequeue(self):
        self.arr.pop(0)
    
    def peek(self):
        