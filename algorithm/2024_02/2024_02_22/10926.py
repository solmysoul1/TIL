T = int(input())
for tc in range(1, T+1):
    arr = list(input())
    cnt = 6
    result = 0
    result_list = []
    while True:
        for n in arr:
            if n == '0':
                cnt -= 1
                if cnt == -1:
                    result_list.append(result)
                    result = 0
                    cnt = 6
            else:
                result += 2**cnt
                cnt -= 1
                if cnt == -1: 
                    result_list.append(result)
                    result = 0
                    cnt = 6
        else:
            break

    print(f'#{tc}', *result_list)
            

    
   
