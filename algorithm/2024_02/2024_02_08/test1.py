def dfs(i, V): # 시작 i, 마지막 V
    visited[i] = 1 # 방문 표시
    print(i) # 출력
    for w in adjl[i]: # i에 인접하고
        if visited[w] == 0: # 방문안한 w가 있으면
            dfs(w)

V, E = map(int,input().split())
arr = list(map(int, input().split()))

# 인접리스트
adjl = [[] for _ in range(V+1)] # ardjl[i] 행에 i에 인접인 정점 번호 저장
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjl[n1].append(n2)
    adjl[n2].append(n1) # 방향이 없는 경우에만 필요
visited = [0]*(V+1)
dfs(1, V)