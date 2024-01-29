'''
강변에 빌딩들이 옆으로 빽빽하게 밀집한 지역이 있다.
이 곳에서는 빌딩들이 너무 좌우로 밀집하여, 강에 대한 조망은 모든 세대에서 좋지만
왼쪽 또는 오른쪽 창문을 열었을 때 바로 앞에 옆 건물이 보이는 경우가 허다하였다.

그래서 이 지역에서는 왼쪽과 오른쪽으로 창문을 열었을때, 양쪽 모두 거리 2이상의 공간이 확보될 때
조망권이 확보된다고 말한다.

빌딩들에 대한 정보가 주어질 때, 조망권이 확보된 세대의 수를 반환하는 프로그램을 작성하시오.

'''

T = 10

for tc in range(1, T+1):
    N = int(input())
    height = list(map(int, input().split()))
    count = 0
    for i in range(2, N-2):
        if height[i] > height[i-2] and height[i] > height[i-1] and height[i] > height[i+1] and height[i] > height[i+2]:
            height_list = [height[i-2], height[i-1], height[i+1], height[i+2]]
            
            max_height = 0       
            for num in height_list:
                if num >= max_height:
                    max_height = num
            count += (height[i] - max_height)
       
    print(f'#{tc} {count}')
