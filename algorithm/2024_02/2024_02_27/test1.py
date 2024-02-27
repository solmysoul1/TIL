# for i in range(1, 4):
#     for j in range(1, 4):
#         for s in range(1, 4):
#             for t in range(1, 4):
#                 print(i,j,s,t)

# ------ 4중 for문 -------


# def KFC(x):
#     KFC(x+1)

# KFC(0)

# ------ 무한 재귀 호출 ------

# def KFC(x):
#     if x == 6:
#         return
#     print(x, end=' ')
#     KFC(x + 1)
#     print(x, end=' ')

# KFC(0)

# ----- 재귀 호출 예제 ------

# path = []

# def KFC(x):
#     if x == 2:
#         print(path)
#         return
#     for i in range(3):
#         path.append(i)
#         KFC(x+1)
#         path.pop()

# KFC(0)

# ----- 중복 순열 ------

# path = []

# def KFC(x):
#     if x == 3:
#         print(path)
#         return
#     for i in range(1, 7):
#         path.append(i)
#         KFC(x+1)
#         path.pop()

# KFC(0)

# ----- 중복 순열 2 -----

# path = []

# def KFC(x):
#     if x == 5:
#         print(path)
#         return
#     for i in range(5):
#         path.append(i)
#         KFC(x+1)
#         path.pop()

# KFC(0)

# ----- 중복 순열 3 -----

path = []
used = [False, False, False]

def KFC(x):
    if x == 2:
        print(path)
        return
    
    for i in range(3):
        if used[i] == True : continue
        used[i] = True
        path.append(i)
        KFC(x+1)
        path.pop()
        used[i] = False

KFC(0)

# ----- 순열 1 -----

# N, T = map(int, input().split())

# path = []

# def KFC(x):
#     if x == N:
#         print(path)
#         return
    
#     for i in range(1, 7):
#         path.append(i)
#         KFC(x+1)
#         path.pop()

# used = [False, False, False, False, False, False, False]

# def MAC(x):
#     if x == N:
#         print(path)
#         return
    
#     for i in range(1, 6):
#         if used[i] == True : continue
#         used[i] = True
#         path.append(i)
#         KFC(x+1)
#         path.pop()
#         used[i] = False

# if T == 1:
    
#     KFC(0)

# if T == 2:

#     MAC(0)

# ----- 중복 순열과 순열 ------

# path = []

# def KFC(x, sum):
#     if x == 3:
#         print(f'{path} = {sum}')
#         return
    
#     for i in range(1, 7):
#         path.append(i)
#         KFC(x+1, sum + i)
#         path.pop()

# KFC(0,0)

# ----- 중복 순열의 누적합 -----

# path = []

# def KFC(x, sum):
#     if x == 3:
#         if sum <= 10:
#             print(f'{path} = {sum}')
#         return
    
#     for i in range(1, 7):
#         path.append(i)
#         KFC(x+1, sum + i)
#         path.pop()

# KFC(0,0)

# ----- sum이 10이하일 때 -----

# path = []

# def KFC(x, sum):
#     if sum < 10:
#         return
#     if x == 3:
#         print(f'{path} = {sum}')
#         return
    
#     for i in range(1, 7):
#         path.append(i)
#         KFC(x+1, sum + i)
#         path.pop()

# KFC(0,0)

# ----- 가지치기 -----

