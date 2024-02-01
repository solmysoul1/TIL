T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    while input_num > N:
        for i in range(N):
            input_num = 1
            for j in range(N):
                arr[i][j] = input_num
                input_num += 1
    while input_num > N*2-1:
        for i in range(1, N):
            input_num = N+1
            arr[i][N] = input_num
            input_num += 1
