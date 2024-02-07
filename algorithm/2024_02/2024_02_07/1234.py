# 비밀번호

for tc in range(1, 11):
    N, M = input().split() # str으로 받음
    pw = list(i for i in M) 
    i = 0
    while i < len(pw)-1:
        if pw[i] == pw[i+1]:
            pw.pop(i)
            pw.pop(i)
            i = 0
        else:
            i += 1
    str_pw = list(map(str, pw))
    print(f'#{tc}', ''.join(str_pw)) # join()은 str일때만 가능
