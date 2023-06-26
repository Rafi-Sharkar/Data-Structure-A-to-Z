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
    
    def stSum(self):
        sum = 0
        while self.arr.isEmpty != True:
            v = self.arr.peek()
            sum += v
            self.arr.pop()
        return sum


    
def check(st1, st2):
    x = st1.stSum()
    y = st2.stSum()

    diff = x-y
    st2.push(diff)


st = stack()
st.push(10)
st.push(15)
st.push(12)
st.push(14)

st1 = stack()
st1.push(12)
st1.push(10)
st1.push(10)
st1.push(10)

st.printStack()
st1.printStack()

check(st,st1)




        
    
    

    

