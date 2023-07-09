# Stack
class Stack:
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

# write code

n = int(input("Enter the limit: "))
stk = Stack()
while n>=0:
    binary = str(bin(n))
    stk.push(binary[2:])
    n-=1
while not stk.isEmpty():
    print(stk.peek())
    stk.pop()


