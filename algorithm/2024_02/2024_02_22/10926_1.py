T = int(input())
for tc in range(1, T+1):
    arr = input()
    result = []
    for i in range(10):
        i *= 7
        result += [int(arr[i:i+7], 2)]
    print(result)

        
    
 

