# 노드의 거리

def bfs(s, N, G): # 시작정점 s, 노드개수 N
    q = [] # 큐
    visited = [0]*(N+1) # visited
    q.append(s) # 시작점 인큐
    visited[s] = 1 # 시작점 방문표시
    while q:  # 큐가 비워질때까지
        t = q.pop(0) # 처리할 정점 디큐
        # t에서 할 일
        if t == G:
            return visited[t]-1 # 최단 경로 간선 수
        for i in adjl[t]: # t에 인접인 정점 i
            if visited[i] == 0: # 방문하지 않은 정점이면
                q.append(i) # 인큐
                visited[i] = 1 + visited[t] # 방문표시
    return 0 # G까지 경로가 없는 경우 (while문이 끝난 경우)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    # 인접리스트
    adjl = [[] for _ in range(V+1)]
    for i in range(E):
        n1, n2 = map(int, input().split())
        adjl[n1].append(n2)
        adjl[n2].append(n1)
        # 무향 그래프
    S, G = map(int, input().split())

    print(f'#{tc} {bfs(S, V, G)}')

