T = int(input())

for tc in range(1, T+1):
    str1 = str(input())
    str2 = str(input())
    count = 0
    if str1 in str2:
        count += 1

    print(f'#{tc} {count}')