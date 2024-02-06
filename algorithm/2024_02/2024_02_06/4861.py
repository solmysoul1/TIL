def f(N, M):
    for i in range(N):
        for j in range(N-M+1):
            if arr[i][j:j+M] == arr[i][i:j+M][::-1]:
                result = arr[i][j:j+M]
                return result
            
    for i in range(N-M+1):
        for j in range(N):
            vertical = ''
            for x in range(i, i+M):
                vertical += arr[x][j]
            if vertical == vertical[::-1]:
                result = vertical
                return result
    return 0

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    result = f(N,M)

    print(f'#{tc} {result}')
