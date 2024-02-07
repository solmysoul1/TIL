for tc in range(1, 11):
    N = int(input())
    arr = [input().split() for _ in range(8)]
    count = 0
    for i in range(8):
        for j in range(8-N+1):
            if arr[i][j:j+N] == arr[i][j:j+N][::-1]:
                count += 1
    
    for i in range(8-N+1):
        for j in range(8):
            vertical = ''
            for k in range(i, i+N):
                vertical += arr[k][j]
            if vertical == vertical[::-1]:
                count += 1

    print(f'#{tc} {count}')

