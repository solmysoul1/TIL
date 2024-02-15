from collections import deque
for tc in range(1, 11):
    T = int(input())
    arr = list(map(int, input().split()))
    Q = deque()
    for n in arr:
        Q.append(n)

    cnt = 1
    while True:
        if Q[-1] <= 0:
            Q[-1] = 0
            break
        for i in range(1, 6):
            Q.append(Q.popleft() - i)
            if Q[-1] <= 0:
                Q[-1] = 0
                break

    print(f'#{tc}', *Q)

    
  
        

        







