# 조합 구하기
def f(i,s,K,M):
    if i == M:
        print(comb)
        return
    else:
        for j in range(s,K-M+i+1):
            comb[i] = j
            f(i+1,j+1,K,M)

M = 3
K = 5
comb = [0]*M
f(0,0,K,M)

