T = int(input())

def count_num(num):
    count = 0
    for i in num_list:
        if i == num:
            count += 1
    return count

for tc in range(1, T+1):
    N, M = input().split()
    num_name = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    num_list = list(map(str, input().split()))

    print(f'#{tc}')
    for n in num_name:
        count_num(n)
        print((n+' ')*count_num(n), end='')




