T = int(input())
for tc in range(T):
    K, N, M  = map(int, input().split())
    chargers = list(map(int, input().split())) 

    busstop = [0] * (N+1) # 정류장이 있는지 정류장별로 표시
    for x in chargers:
        busstop[x] = 1

    bus = 0 # 버스의 현재위치
    count = 0 # 충전횟수

    while bus+K<N: # 마지막 충전 이후 종점에 도착할 수 없으면
        last = 0
        for i in range(bus+1, bus+K+1):
            if busstop[i]:
                last = i
        if last == 0:
            count = 0
            break
        else:
            bus = last
            count += 1

    print(f'#{tc+1} {count}')
