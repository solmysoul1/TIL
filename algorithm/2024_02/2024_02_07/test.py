def push(n):
    global top
    top += 1
    if top==size:
        print('Overflow!')
    else:
        stack[top] = n


top = -1
size = 10
stack = [0]*10

top += 1
stack[top] = 10

top += 1
stack[top] = 20

push(30)

while top>=0:
    top -= 1
    print(stack[top+1])