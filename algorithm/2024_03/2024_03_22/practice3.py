# 2819 격자판의 숫자 이어붙이기
'''
만들 수 있는 서로 다른 7자리 수들의 개수
1. 재귀
2. 7자리까지 반복
3. 중복제거
'''
dy = [0,1,0,-1]
dx = [1,0,-1,0]

def dfs(y,x,path):
    # 기저조건
    if len(path) == 7:
        # 현재까지의 경로 저장
        result.add(path)
        return
    
    for i in range(4):
        new_y = y+dy[i]
        new_x = x+dx[i]
        
        if new_y<0 or new_y >= 4 or new_x < 0 or new_x >= 4:
            continue

        dfs(new_y,new_x,path+maps[new_y][new_x])

T = int(input())
for tc in range(1,T+1):
    # 격자판 저장
    # maps = [list(map(int,input().split())) for _ in range(4)]
    # 갈때마다 경로를 더하기 위해서 문자열로 저장
    maps = [input().split() for _ in range(4)]
    # 중복 제거
    result = set()

    for i in range(4):
        for j in range(4):
            dfs(i,j,maps[i][j])
    print(f'#{tc} {len(result)}')