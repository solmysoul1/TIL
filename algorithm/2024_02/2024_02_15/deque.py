from collections import deque

q = deque()
q.append(1)
q.append(2)

print(q.popleft())
print(q.popleft())

print()

q =[]
for i in range(10000):
    q.append(i)
print('append')
while q:
    q.pop(0)
print('end')

print()

dq = deque()
for i in range(10000):
    dq.append(i)
print('append')
while dq:
    dq.popleft()
print('end')