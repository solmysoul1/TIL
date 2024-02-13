T = int(input())
for tc in range(1, T+1):
    arr = []
    fx = input().split()
    for i in fx:
        if i.isdigit():
            arr.append(int(i))
        elif i in '+-*/':
            if len(arr) >= 2:
                a = arr.pop()
                b = arr.pop()
                if i == '+':
                    arr.append(b+a)
                if i == '-':
                    arr.append(b-a)
                if i == '*':
                    arr.append(b*a)
                if i == '/':
                    arr.append(b/a)
            elif len(arr) < 2:
                print(f'#{tc} error')
                break
        elif i == '.':
            if len(arr) == 1:
                print(f'#{tc} {int(arr.pop())}')
            else:
                print(f'#{tc} error')
                break



