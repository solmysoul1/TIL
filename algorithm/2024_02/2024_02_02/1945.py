T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cnt_a = 0
    cnt_b = 0
    cnt_c = 0
    cnt_d = 0
    cnt_e = 0

    while N != 1:
        if N%2 == 0:
            cnt_a += 1
            N = N/2
        elif N%3 == 0:
            cnt_b += 1
            N = N/3
        elif N%5 == 0:
            cnt_c += 1
            N = N/5
        elif N%7 == 0:
            cnt_d += 1
            N = N/7
        elif N%11 == 0:
            cnt_e += 1
            N = N/11

    print(f'#{tc} {cnt_a} {cnt_b} {cnt_c} {cnt_d} {cnt_e}')

