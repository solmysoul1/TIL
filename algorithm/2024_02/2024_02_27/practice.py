# for a in range(1,4):
#     for b in range(1,4):
#         for c in range(1,4):
#             for d in range(1,4):
#                 print(a,b,c,d)

# ------ 4중 for 문 ------

# def f(x):
#     if x == 6:
#         return
#     print(x, end=' ')
#     f(x+1)
#     print(x, end=' ')

# f(0)

# ------ 재귀 호출 예제 ------

# path = []

# def f(x):
#     if x == 2:
#         print(path)
#         return
    
#     for i in range(3):
#         path.append(i)
#         f(x+1)
#         path.pop()

# f(0)

# ------ 중복 순열 ------

path = []

def f(x):
    if x == 3:
        print(path)
        return
    
    for i in range(1, 7):
        path.append(i)
        f(x+1)
        path.pop()

f(0)


