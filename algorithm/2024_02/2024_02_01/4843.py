T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N):
            if num[min_idx] > num[j]:
                min_idx = j
        num[min_idx], num[i] = num[i], num[min_idx]

    result = []
    for i in range(5):
        result.append(num[-i-1])
        result.append(num[i])
    
    
    print(f'#{tc}', *result)
