T = int(input())

for tc in range(1, T+1):
    num = list(map(int, input()))

    cnt = [0] * 10
    for i in num:
        cnt[i] += 1

    count = 0
    for i in range(10):
        if cnt[i] >= 3:
            count += 1
            cnt[i] -= 3

    for i in range(7):
        if cnt[i] >= 1 and cnt[i+1] >= 1 and cnt[i+2] >= 1: 
            count += 1
            cnt[i] -= 1
            cnt[i+1] -= 1
            cnt[i+2] -=1 

    if count == 2:
        print(f'#{tc} Baby Gin')
    else:
        print(f'#{tc} Lose')
