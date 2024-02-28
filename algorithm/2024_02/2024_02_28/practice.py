# arr = [1,2,3]
# n = len(arr)

# def get_sub(tar):
#     for i in range(n):
#         if tar & 0x1:
#             print(arr[i], end = '')
#     tar >>= 1

# for tar in range(1<<n):
#     print('{', end = '')
#     get_sub(tar)
#     print('}')

# ------ 부분 집합 구현 ------
    
# arr = [1,2,3,4,5]
# n = len(arr)

# def get_sub(tar):
#     for i in range(n):
#         if tar & 0x1:
#             print(arr[i], end=' ')
#     tar >>= 1

# for tar in range(1<<n):
#     print('{', end=' ')
#     get_sub(tar)
#     print('}')

# ------ 부분 집합 구현 ------

# arr = [1,2,3,4,5]

# for a in range(5):
#     for b in range(a+1,5):
#         for c in range(b+1,5):
#             for d in range(c+1,5):
#                 print(arr[a], arr[b], arr[c],arr[d])

# ------ for 문으로 조합 구현 ------

# arr = [1,2,3,4,5]
# path = []
# n = 3

# def run(lev, start):
#     if lev == n:
#         print(path)
#         return

#     for i in range(5):
#         path.append(arr[i])
#         run(lev+1,i+1)
#         path.pop()

# run(0,0)

# ------ 재귀로 조합 구현 ------

# n = 3
# path = []

# def comb(lev, start):
#     if lev == n:
#         print(path)
#         return

#   for i in range(start,7):
#       path.append(i)
#       comb(lev+1,i)
#       path.pop()

# comb(0,1)

# ------ 주사위 조합 ------

# def nCr(n,r,s):
#     if r == 0:
#         print(*comb)
#     else:
#         for i in range(s,n-r+1):
#             comb[r-1] = A[i]
#             nCr(n,r-1,i+1)

# N = 5
# A = [1,2,3,4,5]
# R = 3
# comb = [0]*R

# nCr(N,R,0)

# ------ N개에서 R개의 요소를 고르는 조합 ------

    