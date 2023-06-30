class stack:
    def __init__(self):
        self.arr = []
    
    def push(self,num):
        self.arr.append(num)
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            self.arr.pop()

    def size(self):
        return len(self.arr)

    def isEmpty(self):    
        return self.size()==0

    def printStack(self):
       return self.arr

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"            
        return self.arr[-1]

## write code
st = input()
s=''
stack = stack()
for i in range(len(st)):
    stack.push(st[i])
while not stack.isEmpty():
    s = s+stack.peek()
    stack.pop()
print(s)

