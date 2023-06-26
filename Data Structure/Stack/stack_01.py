# # Stack
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
#         return self.size == 0
#     def printStack(self):
#         print(self.arr)
#     def peek(self):
#         return self.arr[-1]


# st1 = stack()
# st1.push(10)
# st1.push(5)
# st1.push(7)
# st1.push(11)
# st1.printStack()
# st1.pop()
# st1.pop()
# st1.printStack()
# h=10
# def n(h):
#     if h!=0:
#        print(h)
#        return n(h-1)
#     else:
#         print("Done")
# n(h)

for i in range(20):
    print("from for loop",i)
    if(i<5 and i>0):
        print("from condition", i)