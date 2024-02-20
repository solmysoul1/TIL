def pre_order(start):
    global cnt
    if start:
        cnt += 1
        pre_order(left[start])
        pre_order(right[start])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    left = [0]*(max(arr)+1)
    right = [0]*(max(arr)+1)

    for i in range(E):
        if left[arr[i*2]] == 0:
            left[arr[i*2]] = arr[i*2+1]
        else:
            right[arr[i*2]] = arr[i*2+1]
    
    cnt = 0
    pre_order(N)
    print(f'#{tc} {cnt}')



