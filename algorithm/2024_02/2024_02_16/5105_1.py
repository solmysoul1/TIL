def bfs(start):
    q = [start]
    distance = [[0]*N for _ in range(N)]
    di = [0,0,1,-1]
    dj = [1,-1,0,0]
    while q:
        j, i = q.pop(0)
        maze[i][j] = 1
        for s in range(4):
            mj = j + di[s]
            mi = i + dj[s]
            if 0<=mi<N and 0<=mj<N:
                distance[mi][mj] = distance[i][j] + 1
                if maze[mi][mj] == 0:
                    q.append([mj, mi])
                elif maze[mi][mj] == 3:
                    return distance[mi][mj]-1
    return 0
        
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    start = ''
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                start = (j,i) 

    result = bfs(start)
    print(f'#{tc} {result}')
  
