for tc in range(1, 11):
    N = int(input())
    fx = list(map(str, input()))
    total = 0
    for i in fx:
        if i.isdigit():
            total += int(i)
    print(f'#{tc} {total}')