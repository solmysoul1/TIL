# 반복문자 지우기

T = int(input())
for tc in range(1, T+1):
    s = list(map(str, input()))
    n = 0
    while n < len(s)-1:
        if s[n] == s[n+1]:
            s.pop(n)
            s.pop(n)
            n = 0
        else:
            n += 1
    print(f'#{tc}', len(s))


'''
pop() 을 사용하면 계속 리스트의 요소들이 줄어 out of index 에러가 발생함
요소들을 한번 제거 한 후 n 을 0으로 초기화하지 않았던 것도 문제
중복이 되지 않았을 경우 다음 인덱스를 탐색하는 조건식 n += 1 도 누락함
while 문을 어떻게 효율적으로 쓸 것인지 공부가 필요함
'''


            