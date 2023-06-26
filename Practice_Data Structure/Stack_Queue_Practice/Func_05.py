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
    def printStack(self):
        print(self.arr)
    def peek(self):
        return self.arr[-1]
#write code


    def pushstack(self, V):
        temp= stack()
        while self.arr.peek() > V:
            temp.arr.push(self.arr.peek())
            self.arr.pop()
        
        self.arr.push(V)
        while temp.arr.isEmpty() != True:
            self.arr.push(temp.arr.peek())
            temp.arr.pop()





st2 = stack()
