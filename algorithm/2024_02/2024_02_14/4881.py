# 배열 최소합

def f(i, k, s):
    global min_v
    if i == k:
        if min_v > s:
            min_v = s
    elif s >= min_v:
        return
    else:
        for j in range(i, k):
            P[i], P[j] = P[j], P[i] # P[i]<->P[j]
            f(i+1, k, s+arr[i][P[i]])
            P[i], P[j] = P[j], P[i]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    P = [i for i in range(N)]
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_v = 100
    f(0,N,0)
    print(f'#{tc} {min_v}')
    