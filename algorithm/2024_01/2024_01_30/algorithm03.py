T = int(input())
for tc in range(T):

    N = int(input())
    arr = list(map(int, input().split()))

    max_idx = 0
    for i in range(1, N):
        if arr[max_idx] <= arr[i]:
            max_idx = i

    min_idx = 0
    for i in range(1, N):
        if arr[min_idx] > arr[i]:
            min_idx = i

    print(f'#{tc+1} {abs(max_idx - min_idx)}')

