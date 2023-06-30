#Stack
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
        return self.size()==0

    def printStack(self):
       return self.arr

    def peek(self):
        return self.arr[-1]


## Write code







# ({[{(){}}[]]})
#

bracket = input()
open_bracket = ["(","{","["]
stk = stack()

for i in bracket:
    if i in open_bracket:
        stk.push(i)
    else:
        if stk.isEmpty():
            stk.push(i)
            break
        stk.pop()
if stk.isEmpty():
    print("Yes")
else:
    print("No")

