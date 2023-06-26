class Stack:
  def __init__(self):
    self.data = []

  def push(self, val):
    self.data.append(val)

  def pop(self):
    self.data.pop()

  def peek(self):
    val = self.data[-1]
    return val

  def isEmpty(self):
    return len(self.data) == 0

brackets = input()
s = Stack()
for b in brackets:
  if b == '(':
    s.push(b)
  else:
    if s.isEmpty():
      s.push(b)
      break
    s.pop()

if s.isEmpty():
  print('Yes')
else:
  print('No')