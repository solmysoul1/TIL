# 부분집합의 합

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
T = int(input())
for tc in range(1, T+1):
    subset_list = []
    N, K = map(int, input().split())
    for i in range(1<<12):
        li = []
        for j in range(12):
            if i & (1<<j):
                li.append(A[j])
        subset_list.append(li)

    cnt = 0
    for set in subset_list:
        if len(set) == N and sum(set) == K:
            cnt += 1

    print(f'#{tc} {cnt}')