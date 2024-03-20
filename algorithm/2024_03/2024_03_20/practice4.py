graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0]
]

visited = [0]*5

def bfs(start):

    queue = [start]
    visited[start] = 1

    while queue:
        now = queue.pop(0)
        print(now, end=' ')

        # 갈 수 있는 곳 체크
        for to in range(5):
            if graph[now][to] == 0:
                continue
            if visited[to]:
                continue
            visited[to] = 1
            queue.append(to)

bfs(0)