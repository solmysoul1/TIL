T = int(input())
for tc in range(1, T+1):
    N = int(input())
    counts = [0] * 5001 
    
    for i in range(N):
        A, B = map(int, input().split())
        for j in range(A, B+1):
            counts[j] += 1
            
    P = int(input())
    busstop = [int(input()) for _ in range(P)]
    print(f'#{tc}', end=' ')
    
    for i in busstop:
        print(counts[i], end=' ')
    print()