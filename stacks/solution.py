from collections import deque

# creatting a stack

s = []

s.append(1)
s.append(2)
s.append(3)

print(s)
print(s.pop())
print(s.pop())

# using deque

a = deque()
a.append("a")
a.append("b")
a.append("c")

print(a)
print(a.pop())