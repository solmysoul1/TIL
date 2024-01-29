'''
N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초 연산이다.
M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.
다음 줄부터 테스트케이스의 첫 줄에 정수의 개수 N과 구간의 개수 M이 주어진다.
다음 줄에 N개의 정수 a가 주어진다.

[출력]
각 줄마다 #T (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''

T = int(input())

for i in range(T):

    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    
    sum_numbers = []

    for n in range(N-M+1):
        new_list = num_list[n:n+M]
        sum_total = 0
        for num in new_list:
            sum_total += num
        sum_numbers.append(sum_total)
    
    sum_numbers.sort()

    print(f'#{i+1} {sum_numbers[-1]-sum_numbers[0]}')
    


