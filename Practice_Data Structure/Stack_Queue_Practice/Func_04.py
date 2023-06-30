class stack:
    def __init__(self):
        self.arr = []
    
    def push(self,num):
         return self.arr.append(num)
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            return self.arr.pop()
    def size(self):
        return len(self.arr)
    def isEmpty(self):
        return self.size() == 0
    def display(self):
        return self.arr
    def peek(self):
        return self.arr[-1]

# Write code
    # sum stack using method
    def stack_sum(self):
        sum = 0
        while not self.isEmpty():       # why self.arr.isEmpty()  doesn't work
            v = self.pop()
            sum += v
        return sum

# Write code

def balancer(stack1, stack2):
    s1 = stack1.stack_sum()
    s2 = stack2.stack_sum()
    dif = s1 - s2
    return f"By adding {dif} in stack Stack_2 will balance the sum of values of both the stacks"

st1 = stack()
st1.push(10)
st1.push(15)
st1.push(12)
st1.push(14)

st2 = stack()
st2.push(12)
st2.push(10)
st2.push(11)
st2.push(19)

print(st1.display())
print(st2.display())
print(balancer(st1,st2))







        
    
    

    

