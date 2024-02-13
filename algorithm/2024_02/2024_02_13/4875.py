# 미로 안에서 지나갔던 칸은 표시를 해야함
def f(i, j, N):
    stack = [] # 지나간 경로 저장
    maze[i][j] = 1 # 시작점 방문 표시 
    while True:
        maze[i][j] = 1 # 방문한 칸에 표시
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj] != 1:
                if maze[ni][nj] ==3:
                    return 1
                stack.append((i, j)) # 현재칸 push
                i, j = ni, nj
                break
        else: # 지나온 경로에서 다시 시작해야 하는 경우
            if stack:
                i, j = stack.pop()
            else:
                return 0
            

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    # 시작점 찾기
    sti = stj = -1
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sti, stj = i, j
                break
        if sti != -1:
            break

    # 미로찾기
    result = f(sti, stj, N)
    print(f'#{tc} {result}')



# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input())) for _ in range(N)]
#     di = [0,0,-1,1]
#     dj = [-1,1,0,0]
#     start = [0,0]
#     end = [0,0]
#     st = []
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 2:
#                 start = [i,j]
#             elif arr[i][j] == 3:
#                 end = [i,j]
#             arr[start[0]][start[1]] = -1
#             for k in range(4):
#                 mi = di[k] + start[0]
#                 mj = dj[k] + start[1]
#                 if 0<=mi<N and 0<=mj<N and (arr[mi][mj] == 0 or arr[mi][mj] == 3):
#                     st.append((i, j))
#                     arr[mi][mj] = -1
#                     i = mi
#                     j = mj
#                     break
#             else:
#                 if st:
#                     i, j = st.pop()
#                 else:
#                     break
#     if arr[end[0]][end[1]] == -1:
#         print(f'#{tc} 1')
#     else: 
#         print(f'#{tc} 0')

