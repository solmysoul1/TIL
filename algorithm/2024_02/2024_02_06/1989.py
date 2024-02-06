T = int(input())
for tc in range(1, T+1):
    word_list = list(input())
    word_reverse = []
    for i in word_list[::-1]:
        word_reverse.append(i)
    a = ''.join(word_list)
    b = ''.join(word_reverse)
    if a == b :
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
    