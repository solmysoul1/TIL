# 회전
from collections import deque

# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = list(map(int, input().split()))
#     result = arr[M%N]
#     print(f'#{tc} {arr[M%N]}')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    Q = deque()
    for n in arr:
        Q.append(n)
    for i in range(M):
        Q.append(Q.popleft())

    print(f'#{tc} {Q.popleft()}')




