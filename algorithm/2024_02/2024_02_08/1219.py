def dfs(s, e): # s출발, e도착
    visited = [0]*100 # visited, stack 생성 및 초기화
    stack = []
    visited[s] = 1 # 시작점 방문 표시
    v = s # 현재 방문 위치 v
    while True:
        w = A[v] # 첫번째 인접 도시
        if A[v] != -1 and visited[w] == 0: # 현재 방문위치 v에 인접한 w
            stack.append(v)# 지나간 칸을 스택에 저장하고 이동
            v = w
            visited[v] = 1
            if v == e:
        elif B[v] != -1 and visited[B[v]] == 0:
                stack.append(w)
                v = w
                visited[v] = 1
        else: # 지나온 곳에서 다시 탐색 
            if stack:
                v = stack.pop()
            else: # 출발지까지 거슬러와서 가능한 모든 곳을 확인한 경우
                break
        if v == e:
            return 1


for _ in range(10):
    tc, E = map(int, input().split())
    arr = list(map(int, input().split()))

    A = [-1]*100 # A[i] i에 인접한 도시번호
    B = [-1]*100 # B[i] i에 인접한 도시번호
    
    for i in range(0, E*2, 2):
        n1, n2 = arr[i], arr[i+1] # n1->n2 도로가 있음
        if A[n1] == -1:
            A[n1] = n2
        else:
            B[n1] = n2
    dfs(0, 99)



