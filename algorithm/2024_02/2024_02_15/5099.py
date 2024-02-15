# 피자 굽기

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N : 화덕의 크기 M : 피자 개수
    pizza = list(map(int, input().split()))
    pz = []
    for idx, value in enumerate(pizza):
        pz.append([idx, value])
    oven = pz[:N]
    rest_pz = pz[N:]
    while len(oven) > 1:
        check = oven.pop(0)
        # check[1]//=2
        check[1] //= 2
        if check[1] == 0:
            if rest_pz:
                oven.insert(0,rest_pz.pop(0))
        else:
            oven.append(check)
    
    print(f'#{tc}', oven[0][0]+1)
                    
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     pizza = list(map(int, input().split()))

#     oven = []
#     for i in range(N):
#         oven.append(i)
#     next = N

#     while oven:
#         tmp = oven.pop(0)
#         pizza[tmp] //= 2
#         if pizza[tmp] > 0:
#             oven.append[tmp]
#         elif next < M:
#             oven.append(next)
#             next += 1
#     print(f'#{tc} {tmp+1}')

