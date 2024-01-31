T = int(input())

for tc in range(1, T+1):
    area = [[0 for _ in range(10)] for _ in range(10)]
    count = 0
    N = int(input())
    for i in range(1, N+1):
        row1, col1, row2, col2, color = map(int, input().split())

        for row in range(row1, row2+1):
            for col in range(col1, col2+1):
                if color == 1:
                    if area[row][col] == 0:
                        area[row][col] = 1
                    elif area[row][col] == 2:
                        area[row][col] = 3
                        count += 1

                else:
                    if area[row][col] == 0:
                        area[row][col] = 2
                    elif area[row][col] == 1:
                        area[row][col] = 3
                        count += 1 
    print(f'#{tc} {count}')

    