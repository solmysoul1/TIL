T = int(input())
for tc in range(1, T+1):
    A, B = input().split()
    N = len(A)
    M = len(B)
    cnt = 0
    i = 0
    j = 0
    while i <= N-M:
        if A[i+j] == B[j]:
            j += 1
            if j == M:
                cnt += 1
                j = 0
                i += M
        else:
            j = 0
            i += 1
    print(f'#{tc} {N-M*cnt+cnt}')
