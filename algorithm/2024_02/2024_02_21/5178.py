T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = [0]*(N+1)
   
    for _ in range(M):
        S, T = map(int, input().split())
        arr[S] = T

    for i in range(N, 0, -1):
        arr[i//2] += arr[i]

    print(f'#{tc}', arr[L])
    