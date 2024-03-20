graph = [
    [1, 3],
    [0, 2, 4],
    [1],
    [0, 4],
    [1, 3]
]
visited = [0]*5
path = []

def dfs(now):
    # 기저 조건

    # 다음 재귀 호출 전
    # visited[now] = 1
    # path.append(now)

    # 다음 재귀 호출
    # dfs: 현재 노드에서 다른 노드들을 확인
    for to in graph[now]:
        # 이미 방문했다면 pass
        if visited[to]:
            continue
        
        visited[to] = 1
        path.append(to)
        dfs(to)

    # 돌아왔을 때 작업
visited[0] = 1
path.append(0)
dfs(0)
print(path)
