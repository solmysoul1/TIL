'''
4828. min max

N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.

[입력]
첫 줄에 테스트 케이스의 수 T가 주어진다. (1<= T <= 50)
각 케이스의 첫 줄에 양수의 개수 N이 주어진다. (5<= N <= 1000)
다음 줄에 N개의 양수 a가 주어진다. (1<= a <= 1000000)

[출력]
각 줄마다 #T (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''

T = int(input())

for i in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))

    max_num = 0
    min_num = num_list[0]

    for n in num_list:

        if n >= max_num:
            max_num = n
        if n <= min_num:
            min_num = n
            
    print(f'#{i+1} {max_num - min_num}')
