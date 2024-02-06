# 픙선팡

T = int(input())

di = [0,0,-1,1] # 상 하 좌 우
dj = [-1,1,0,0]

for tc in range(1, T+1):
    N, M = map(int, input().split())
    flower_map = [list(map(int, input().split())) for _ in range(N)]