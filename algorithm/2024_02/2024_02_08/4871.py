# 그래프 경로
def dfs(S, V, G): 
    visited = [0]*(V+1) # 방문 여부 확인 
    st = [] # 스택 역할을 할 리스트 생성
    visited[S] = 1 # 시작점 방문 처리
    result = 0 # 기본 결과 값을 0으로 지정
    while True: 
        for w in adjl[S]:
            if visited[w] == 0:
                S = w
                st.append(S)
                visited[S] = 1
                break
        else:
            if st:
                S = st.pop()
            else:
                break
        if S == G:
            result = 1
            break
        else: 
            result = 0
    return result 

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split()) # 노드의 개수와 간선 정보의 개수
    adjl = [[] for _ in range(V+1)] # 노드의 개수만큼 빈 리스트 생성 각 번호마다 연결된 노드를 저장
    for n in range(E): 
        a, b = map(int, input().split()) # 간선 정보
        adjl[a].append(b) # adjl의 a번 인덱스에 b를 저장
    S, G = map(int, input().split()) # 탐색할 시작점과 끝점
    print(f'#{tc} {dfs(S, V, G)}')