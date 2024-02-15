# 세개의 데이터 1, 2, 3 을 순서대로 삽입하고 1, 2, 3 순서대로 반환하기

N = 3
Q = [0] * N
queue = []

for i in range(N):
    Q[i] = i + 1 

for i in range(N):
    print(Q[i])

print()

queue.append(1)
queue.append(2)
queue.append(3)

while queue:
    print(queue.pop(0))

print()

N = 10
q = [0] * 10
front = rear = -1

rear += 1
q[rear] = 10

rear += 1
q[rear] = 20

rear += 1
q[rear] = 30

while front != rear: # 큐가 비어 있지 않으면
    front += 1
    print(q[front])
