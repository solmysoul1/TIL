# 이진 힙
def enq(n):
    global last
    last += 1 
    h[last] = n 
    c = last 
    p = c//2 
    while p and h[p]>h[c]: 
        h[p], h[c] = h[c], h[p]
        c = p
        p = c//2

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    h = [0]*(N+1) 
    last = 0

    while True:
        for n in num_list:
            enq(n)
        if num_list.index(n) == len(num_list)-1:
            break

    total = 0
    while last != 0:
        last //= 2
        total += h[last]
    
    print(f'#{tc} {total}')


    
