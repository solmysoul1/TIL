# T = int(input())
# for tc in range(1, T+1):
#     N, M, K = map(int, input().split())
#     arrive = list(map(int, input().split()))
#     arrive.sort()

#     made_bread = 0
#     sold_bread = 0
#     result = 0
#     for i in range(len(arrive)):
#         made_bread = arrive[i]//M*K
#         remain = made_bread - sold_bread
#         if remain >= 1:
#             sold_bread += 1
#             pass
#         else:
#             result = 1
#     if result == 0:
#         print(f'#{tc} Possible')
#     else: 
#         print(f'#{tc} Impossible')
        

# ------ swea 1860 진기의 최고급 붕어빵 ------
    
# def start():
#     sold_bread = 0
#     for person in customers:
#         made_bread = (person//m) * K

#         sold_bread -= 1

#         remain = made_bread - sold_bread

#         if remain < 0:
#             return 'Impossible'
#     return 'Possible'

# T = int(input())
# for tc in range(1, T+1):
#     n, m, k = map(int,input().split())
#     customers = list(map(int,input().split()))
#     customers.sort()
#     result = start()

#     print(f'#{tc} {result}')
    
# ------ 붕어빵 답안 ------
        
# for tc in range(1,11):
#     N = int(input())

# ------ 1220 Magnetic ------
    
# def get_sero_cnt(col):
#     cnt = 0
#     # red 자성체를 체크
#     is_red = False

#     for row in range(N):
#         # 1. red 자성체 발견
#         if arr[row][col] == 1:
#             is_red = True
#         # 2. 이전에 red 자성체를 발견했고, 현재 blue 자성체 발견 cnt += 1
#         elif is_red and arr[row][col] == 2:
#             cnt += 1
#             is_red = False # 갱신

#     return cnt

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     total_cnt = 0
#     for col in range(N):
#         total_cnt += get_sero_cnt(col)
#     print(f'#{tc} {total_cnt}')
    
# ------ Magnetic 답안 ------
    
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())

# ------ 4408 자기 방으로 돌아가기 ------
    
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     # 복도 리스트 초기화
#     corridor = [0] * 400
#     max_v = 0

#     for _ in range(N):
#         # 현재방 s, 돌아갈 방 e
#         s, e = map(int,input().split())

#         # 특징 2번 아랫방을 윗방으로 변경
#         if s % 2 == 0:
#             s -= 1
#         if e % 2 == 0:
#             e -= 1

#         # 특징 1번 출발지보다 목적지가 더 큰 값이 되도록 swap
#         if s > e : s, e = e, s

#         for i in range(s, e+1):
#             corridor[i] += 1
#             max_v = max(corridor[i], max_v)
#         print(f'#{tc} {max_v}')

# ------ 4408 자기 방으로 돌아가기 답안 ------

# T = int(input())
# for tc in range(1, T+1):
#     n = int(input())
#     arr = [input() for _ in range(n)]

# ------ 11315 오목 판정 ------
    
# def omok(y,x):
#     # 방향배열
#     dy = [1,0,1,-1] # 아래, 오른쪽, 4시방향(대각선), 2시방향(대각선)
#     dx = [0,1,1,1]

#     # 네방향 탐색
#     for bang in range(4):
#         cnt = 1 # 기준 좌표에 돌이 있으면 cnt = 1 부터 시작
#         # 돌 4개를 탐색
#         for power in range(1,5):
#             ny = y + (dy[bang] * power)
#             nx = x + (dx[bang] * power)
#             if not (0<ny<=n and 0<nx<=n): break
#             # 돌을 발견하면 count
#             if arr[ny][nx] == 'o' : cnt += 1

#             if cnt == 5:
#                 return True
#     return False

# def game_start():
#     for r in range(n):
#         for c in range(n):
#             if arr[r][c] == 'o':
#                 if omok(r,c):
#                     return 'YES'
#     return 'NO'

# T = int(input())
# for tc in range(1, T+1):
#     n = int(input())
#     arr = [input() for _ in range(n)]
#     result = game_start()
#     print(f'#{tc} {result}')

# ------ 11315 오목 판정 답안 ------



# ------ 4615 재밌는 오셀로 게임 ------
    
# B = 1 # 흑돌
# W = 2 # 백돌
# # 반대돌의 색 1->2, 2->1

# di = [0,1,0,-1,1,1,-1,-1]
# dj = [1,0,-1,0, 1,-1,-1,1]
# op = [0,2,1] # 반대편 돌의 색 op[bw]

# def f(i,j,wb,N): # i, j 돌을 놓을 행, 열 . wb 돌의 색, N 게임판 크기
#     board[i][j] = wb # board[i][j]  에 wb 돌 놓기
#     # 8개의 방향에 대해서 뒤집을 수 있는지 확인
#     for k in range(8):
#         flip = [] # 같은 색 돌을 만나면 뒤집을 위치 저장
#         ni, nj = i+di[k], j+dj[k]
#         while 0<=ni<N and 0<=nj<N and board[ni][nj] == op[wb]: # ni,nj에 반대색 돌이 있으면 이동
#             flip.append((ni,nj)) # 뒤집을 후보
#             ni, nj = ni+di[k], nj+dj[k] # 이동
#         if 0<=ni<N and 0<=nj<N and board[ni][nj] == wb: # 같은 색을 만나서 중단된 경우
#             for p,q in flip: # 중간에 있는 돌을 뒤집기
#                 board[p][q] = wb

# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int,input().split())
#     play = [list(map(int, input().split())) for _ in range(M)] # 열,행,돌 돌을 놓는 정보 저장

#     board = [[0]*N for _ in range(N)] # 인덱스를 0부터 시작 (문제입력은 1부터)
#     board[N//2-1][N//2-1] = W # 4개의 돌 놓기
#     board[N//2-1][N//2] = B
#     board[N//2][N//2-1] = B
#     board[N//2][N//2] = W
    
#     for j, i, wb in play:
#         f(i-1,j-1,wb, N) # 돌을 놓는 함수, 입력은 인덱스 1부터 처리는 인덱스 0부터
    
#     cnt_b = cnt_w = 0
#     for i in range(N):
#         for j in range(N):
#             if board[i][j] == W:
#                 cnt_w += 1
#             elif board[i][j] == B:
#                 cnt_b += 1

#     print(f'#{tc} {cnt_b} {cnt_w}')

# ------ 4615 재밌는 오셀로 게임 답안 ------
    

