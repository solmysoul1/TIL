# arr = ['A', 'B', 'C']
# n = len(arr)

# def get_sub(tar):
#     for i in range(n):
#         if tar & 0x1:
#             print(arr[i], end='')
#         tar >>= 1

# for tar in range(1<<n):
#     print('{', end='')
#     get_sub(tar)
#     print('}')

# ------ 부분 집합 구현 ------

# arr = ['A', 'B', 'C', 'D', 'E']
# n = len(arr)

# def get_count(tar):
#     cnt = 0
#     for i in range(n):
#         # 1비트가 1인지 확인
#         if tar & 0x1:
#             cnt += 1
#         # right shift 비트 연산자 -> 오른쪽 끝 비트를 하나씩 제거
#         tar >>= 1
#     return cnt

# result = 0
# for tar in range(1<<n):
#     if get_count(tar) >= 2: # bit가 2개 이상 1이라면 -> 2명 이상이라면
#         result += 1
# print(result)

# ------ 부분 집합 구현 ------

# arr = ['A', 'B', 'C', 'D', 'E']

# for a in range(5):
#     start1 = a + 1
#     for b in range(start1,5):
#         start2 = b + 1
#         for c in range(start2, 5):
#             print(arr[a], arr[b], arr[c])

# ------ 3중 for 문으로 조합 구현 ------

# arr = ['A', 'B', 'C', 'D', 'E']
# path = []

# n = 3
# def run(lev, start):
#     if lev == n:
#         print(path)
#         return
    
#     for i in range(5):
#         path.append(arr[i])
#         run(lev+1, i+1)
#         path.pop()
           
# run(0,0)

# ------ 재귀로 조합 생성 ------

# N = 3
# path = []

# def func(lev, start):
#     if lev == N:
#         print(path)
#         return

#     for i in range(start, 7):
#         path.append(i)
#         func(lev+1, i)
#         path.pop()

# func(0,1)

# ------ 주사위 조합 ------

# N = 5
# for i in range(N-1):
#     for j in range(i+1,N):
#         print(i,j)

# ------ N개에서 2개를 고르는 조합 ------

# def nCr(n,r,s):
#     if r == 0:
#         print(*comb)
#     else:
#         for i in range(s,n-r+1):
#             comb[r-1] = A[i]
#             nCr(n,r-1,i+1)

# N = 5
# A =[1,2,3,4,5]
# R =3
# comb = [0]*R

# nCr(N,R,0)

# ------ n개에서 r개를 고르는 조합, s선택할 수 있는 구간의 시작 ------
        
# arr = [15,30,50,10]
# s = 0
# arr.sort()
# for i in range(4):
#     s += arr.pop(0)*len(arr)

# print(s)

# ------ 그리디 ------

# n = 3
# target = 30
# things = [(5,50), (10,60), (20,140)]
# # kg당 가격으로 내림차순 정렬
# things.sort(key = lambda x:(x[1]/x[0]), reverse=True)

# sum = 0
# for kg, price in things:
#     per_price = price/kg
#     # 만약 가방에 남은 용량이 얼마 되지 않는다면, 물건을 잘라 가방에 넣고 끝냄
#     if target < kg:
#         sum += target * per_price
#         break

#     sum += price
#     target -= kg

# print(int(sum))

# ------ 그리디 도둑 문제 ------

# N = 10
# # 종료 시간 기준으로 오름차순 정렬
# schedule = [(1,4),(3,5),(1,6),(5,7),(3,8),(5,9),(6,10),(8,11),(2,13),(12,14)]
# schedule.sort(key=lambda x:x[1])
# cnt = 0
# fi = 0 # 진행중인 회의 종료시간
# room = []
# for i in range(N): # i번 회의에 대해
#     # i번 회의를 선택하려면, si>= fi 현재 진행중인 회의 이후에 시작
#     if schedule[i][0] >= fi:
#         cnt += 1
#         fi = schedule[i][1] # 새 회의 종료시간
#         room.append((schedule[i][0],schedule[i][1]))
    
# print(cnt)
# print(room)

# ------ 그리디 회의실 문제 : 백준 1931 ------




