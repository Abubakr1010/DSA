from collections import deque

# using list but removing elements from from front require shifting all other element 
# making it O(n)

q = []
q.append(1)
q.append(2)

print(q)
print(q.pop())

# using q which is efficient way making them A(1) time complexity

s = deque()
s.append("a")
s.append("b")
s.append("c")

print(s)
print(s.popleft())
print(s[-1])

# add mutiple element to right of queue
s.extend(['d','e'])
print(s)

# add multiple element at left
s.extendleft(['y','z'])
print(s)

# remove occurance of a value
s.remove('y')
print(s)

# we can also use count, reverse also