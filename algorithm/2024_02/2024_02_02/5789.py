T = int(input())


for tc in range(1, T+1):
    N, Q = map(int, input().split())

    num = [0 for _ in range(N)]

    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for b in range(L-1, R):
            num[b] = i

    print(f'#{tc}', *num)