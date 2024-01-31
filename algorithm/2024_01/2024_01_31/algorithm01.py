'''
1부터 12까지의 숫자를 원소로 가진 집합 A가 있다. 집합 A의 부분 집합 중 N개의 원소를 갖고 있고,
원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.

해당하는 부분 집합이 없는 경우 0을 출력한다.

'''

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split()) 

    arr = [i for i in range(1, 13)]
    result = 0

    for i in range(1<<12):
        sum_sub = 0
        subset = []

        for j in range(12):
            if i & (1<<j):
                sum_sub += arr[j]
                subset.append(arr[j])
        if len(subset) == N and sum_sub == K:
            result += 1
            
    print(f'#{tc} {result}')

