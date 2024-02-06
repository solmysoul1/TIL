T = int(input())
for tc in range(1, T+1):
    A, B = map(str, input().split())
    M = len(A)
    N = len(B)
    count = 0
    i = 0

    while i <= M - N:
        if A[i:i+N] == B:
            count += 1
            i += N
        else:
            count += 1
            i += 1
    if i < M:
        count += M - i
    
    print(f'#{tc} {count}')
   
            
