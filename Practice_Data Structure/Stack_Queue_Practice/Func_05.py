class stack:
    def __init__(self):
        self.arr = []
    
    def push(self,num):
        self.arr.append(num)
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            self.arr.pop()
    def size(self):
        return len(self.arr)
    def isEmpty(self):
        return self.size() == 0
    def display(self):
        return self.arr
    def peek(self):
        return self.arr[-1]

#write code
    def pushstack(self, V):
        temp= stack()
        while not self.isEmpty() and self.peek() > V:
            temp.push(self.peek())
            self.pop()
        
        self.push(V)
        while not temp.isEmpty():
            self.push(temp.peek())
            temp.pop()

st1 = stack()
st1.push(10)
st1.push(15)
st1.push(12)
st1.push(14)
print(st1.display())
st1.pushstack(9)
print(st1.display())