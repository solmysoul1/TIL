arr = [1,2,3]
n = len(arr)

def get_sub(tar):
    for i in range(n):
        if tar & 0x1:
            print(arr[i], end = '')
        tar >>= 1

for tar in range(1<<n):
    print('{', end = '')
    get_sub(tar)
    print('}')

    