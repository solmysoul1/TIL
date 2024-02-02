T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = [i for i in map(int, input())]

    count = 0
    cnt_list = []

    for i in num:
        if i == 1:
            count += 1
        else:
            count = 0
        cnt_list.append(count)

    max_cnt = 0
    for n in cnt_list:
        if n > max_cnt:
            max_cnt = n

    print(f'#{tc} {max_cnt}')
