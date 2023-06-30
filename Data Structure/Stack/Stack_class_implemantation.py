# Stack
class stack:
    def __init__(self):     # initializing the stack
        self.arr = []
    #push
    def push(self, value):
        return self.arr.append(value)
    #pop
    def pop(self):
        if self.isEmpty():
            return "Srack is empty"
        return self.arr.pop()
    #lenght
    def size(self):
        return len(self.arr)
    #isEmpty
    def isEmpty(self):
        return self.size() == 0
    #peek
    def peek(self):
        if self.isEmpty():
            return "Stake is empty"
        return self.arr[-1]
    #stack print
    def stackPrint(self):
        return self.arr
    
# Write code

st1 = stack()
st1.push(13)
st1.push(7)
st1.push(3)
st1.push(31)
st1.push(11)
print(st1.stackPrint())
print("\n")
st1.pop()
print(st1.stackPrint())
st1.pop()
print(st1.stackPrint())
st1.pop()
print(st1.stackPrint())
print(st1.isEmpty())
print(st1.peek())
print(st1.size())