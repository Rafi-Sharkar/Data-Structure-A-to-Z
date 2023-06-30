# Queue
class Queue:
    def __init__(self):     # create a queue 
        self.arr = []
    # enqueue
    def enqueue(self, value):
        return self.arr.append(value)
    # dequeue
    def dequeue(self):
        return self.arr.pop(0)
    # display
    def display(self):
        return self.arr
    # size
    def size(self):
        return len(self.arr)
    # isEmpty
    def isEmpty(self):
        return self.size()==0
    # peek
    def peek(self):
        return self.arr[0]

# write code

# Volunteer A contain even and B contain odd number's of ID
Volunteer_A = Queue()
Volunteer_B = Queue()

# id = int(input("Enter your id: "))

list_id = list(map(int,input("Enter the list numvers separated by space: ").split(" ")))
print("user list",list_id)
for id in list_id:
    if id%2 == 0:
        Volunteer_A.enqueue(id)
    else:
        Volunteer_B.enqueue(id)
print("Volunteer_A",Volunteer_A.display())
print("Volunteer_B",Volunteer_B.display())