T = int(input()) 

for t in range(T): 
    N = int(input())
    num_list = list(map(int, input()))

    cnt = [0] * 10
    for i in range(N):
        cnt[num_list[i]] += 1 

    max_cnt = 0
    for k in range(10):
        if max_cnt <= cnt[k]:
            max_cnt = cnt[k]
            idx = k
    
    print(f'#{t+1} {idx} {max_cnt}')
        


