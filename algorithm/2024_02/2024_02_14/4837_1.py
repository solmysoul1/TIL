def f(i, k, t):
    global result
    count = 0
    if i == k:
        ss = 0
        for j in range(k):
            if bit[j]:
                ss += arr[j]
        if ss == t:
            count = 0
            for j in range(k):
                if bit[j]:
                    count += 1
        if count == N:
            result += 1
    else:
        for j in range(1, -1, -1):
            bit[i] = j
            f(i+1, k, t)
            
    return result

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    bit = [0]*12
    result = 0
    print(f'#{tc}', f(0, 12, K))