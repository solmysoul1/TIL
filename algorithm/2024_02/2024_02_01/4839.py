T = int(input())

for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    arr = list(range(1, P+1)) 
    
    Pa_cnt = 0
    start = 1
    end = P

    while start <= end:
        middle = (start+end)//2
        Pa_cnt += 1
        if Pa == middle:
            break
        elif Pa > middle:
            start = middle 
        else:
            end = middle

    start = 1
    end = P
    Pb_cnt = 0

    while start <= end:
        middle = (start+end)//2
        Pb_cnt += 1
        if Pb == middle:
            break
        elif Pb > middle:
            start = middle        
        else:
            end = middle    
    
    if Pa_cnt > Pb_cnt:
        print(f'#{tc} B')
    elif Pa_cnt < Pb_cnt:
        print(f'#{tc} A')
    else:
        print(f'#{tc} 0')



