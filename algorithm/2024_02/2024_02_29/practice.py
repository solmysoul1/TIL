# ------ 진기의 최고급 붕어빵 ------ 

# def boong():
#     sold_bread = 0
#     for p in arrive:
#         made_bread = p//M*K
#         remain = made_bread - sold_bread
#         if remain > 0:
#             sold_bread += 1
#         else:
#             return 'Impossible'
#     else:
#         return 'Possible'

# T = int(input())
# for tc in range(1, T+1):
#     N, M, K = map(int, input().split())
#     arrive = list(map(int, input().split()))
#     arrive.sort()
#     result = boong()
#     print(f'#{tc} {result}')

# ------ Magnetic ------

# def get_sero_cnt(col):
#     cnt = 0
#     is_red = False

#     for row in range(N):
#         if arr[row][col] == 1:
#             is_red = True
#         elif is_red and arr[row][col] == 2:
#             cnt += 1
#             is_red = False

#     return cnt

# for tc in range(1, 11):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     total_cnt = 0
#     for col in range(N):
#         total_cnt += get_sero_cnt(col)
    
#     print(f'#{tc} {total_cnt}')

# ------ 오목 판정 ------



    

        

