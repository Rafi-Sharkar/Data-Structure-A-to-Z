#Stack
# class stack:
#     def __init__(self):
#         self.arr = []
    
#     def push(self,num):
#         self.arr.append(num)
#     def pop(self):
#         if self.isEmpty():
#             print("Stack is empty")
#         else:
#             self.arr.pop()

#     def size(self):
#         return len(self.arr)

#     def isEmpty(self):    
#         return self.size()==0

#     def printStack(self):
#        return self.arr

#     def peek(self):
#         return self.arr[-1]


## Write code

# bracket = input()
# br = ""
# open_bracket = ["(","{","["]
# st1 = stack()
# for i in range():
#     if i in open_bracket:
#         st1.push()
#     else:
#         if st1.isEmpty():
#             st1.push()
#         st1.pop()
# if st1.isEmpty():
#     print("Yes")
# else:
#     print("No")
def sum(n):
    sum=0
    num=n
    while num!=0:
        sum=sum+(num%10)
        num=num//10
    return sum
print(sum(1234))