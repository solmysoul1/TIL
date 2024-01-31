for tc in range(10):
    n = int(input())
    boxes = list(map(int, input().split()))
 
    def min_max():
        max_idx = 0
        min_idx = 0
        for idx in range(1, 100):
            if boxes[idx] > boxes[max_idx]:
                max_idx = idx
            if boxes[idx] < boxes[min_idx]:
                min_idx = idx
        return max_idx, min_idx
 
    while True:
        max_idx, min_idx = min_max()
        boxes[max_idx] -= 1
        boxes[min_idx] += 1
        n -= 1
 
        if n <= 0:
            break
    max_idx, min_idx = min_max()
    print(f'#{tc+1} {boxes[max_idx] - boxes[min_idx]}')