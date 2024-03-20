graph = [
    [1, 3],
    [0, 2, 4],
    [1],
    [0, 4],
    [1, 3]
]

visited = [0]*5

def bfs(start):

    queue = [start]
    visited[start] = 1

    while queue:
        now = queue.pop(0)
        print(now, end=' ')

        # 갈 수 있는 곳 체크
        for to in graph[now]:
    
            if visited[to]:
                continue
            
            visited[to] = 1
            queue.append(to)

bfs(0)