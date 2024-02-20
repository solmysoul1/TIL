# 이진탐색
def in_order(T, N):
    global cnt
    if T<=N:
        in_order(T*2, N)
        tree[T] = cnt
        cnt += 1
        in_order(T*2+1, N)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0]*(N+1) # 비어있는 완전 이진트리
    cnt = 1
    in_order(1, N)
    print(f'#{tc} {tree[1]} {tree[N//2]}')