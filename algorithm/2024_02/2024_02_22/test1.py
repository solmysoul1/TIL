N = int(input())

arr = [[0]*7 for _ in range(2)]

n1 = 1
for i in range(4):
    arr[0][i] = n1
    n1 += 1

n2 = N
for j in range(4):
    arr[1][7-j-1] = n2
    n2 -= 1

print(arr[0])
print(arr[1])