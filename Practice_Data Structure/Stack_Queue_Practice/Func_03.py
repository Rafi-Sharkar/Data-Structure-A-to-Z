# Stack
class Stack:
    def __init__(self):
        self.stack = []

    def isempty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.isempty():
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if not self.isempty():
            return self.stack[-1]
        else:
            return None

    def size(self):
        return len(self.stack)
    
    def display(self):
        return self.stack

# write code

def keepLargestOnTop(stk):
    hsk = Stack()   
    max = stk.pop()
    while not stk.isempty():
        if max <= stack.peek():
            hsk.push(max)
            max = stack.pop()
        else:
            hsk.push(stk.pop())
    while not hsk.isempty():
        stk.push(hsk.pop())
    stk.push(max)
    return stk

# input

x = [4,14,42,12,9]
stack = Stack()
for i in x:
    stack.push(i)

print("Input: ",end="")
print(stack.display())
print("Output: ",end="")
stack = keepLargestOnTop(stack)
print(stack.display())
