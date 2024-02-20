# 중위순회
def inorder(root):
    if root:
        print(left)
        inorder(left[root])
        result.append(arr[root-1][1])
        inorder(right[root])

for tc in range(1, 11):
    N = int(input())
    arr = list(input().split() for _ in range(N))
    par = [0]*(N+1)
    left = [0]*(N+1)
    right = [0]*(N+1)
    result = []

    for i in arr:
        par[int(i[0])] = i[1]
        if len(i) == 3:
            left[int(i[0])] = int(i[2])
        elif len(i) == 4:
            left[int(i[0])] = int(i[2])
            right[int(i[0])] = int(i[3])
    
    inorder(1)
    print(f'#{tc}', ''.join(result))
