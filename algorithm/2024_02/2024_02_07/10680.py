# 괄호 검사
T = int(input())
for tc in range(1, T+1):
    code = input()
    stack = []
    result = 0
    for i in code:
        if i == '{' or i == '(' :
            stack.append(i)
        elif i == '}' or i == ')':
            if stack != []:
                if (i == '}' and stack[-1] == '{') or (i == ')' and stack[-1] == '('):
                    stack.pop()
                else:
                    break
            else:
                break
    else:    
        if stack == []:
            result = 1

    print(f'#{tc} {result}')

'''
13번 라인 stack.pop()에서 빈 리스트일 경우 pop을 실행하지 못해 발생하는 에러로 인해
런타임 에러 발생
위와 같은 문제를 해결하기 위해 stack이 빈리스트가 아닐 경우를 조건으로 추가함
19번 라인 if stack : 과 같은 True False 로 조건을 걸지 않고 if stack == [] 로 
조건을 추가함 
'''
