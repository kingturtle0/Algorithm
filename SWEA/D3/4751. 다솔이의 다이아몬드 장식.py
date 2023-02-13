def diamond(x, arr, direct):
    for i in range(8):
        dy = 2 + direct[i][0]
        dx = x + direct[i][1]
        arr[dy][dx] = '#'

T = int(input())

for tc in range(T):
    mystr = input()
    n = len(mystr)

    size = (5*n)-(n-1)
    arr = [['.' for _ in range(size)] for _ in range(5)]
    direct = [[-2,0],[2,0],[0,-2],[0,2],[-1,-1],[-1,1],[1,-1],[1,1]]

    idx = 0
    for i in range(2, size, 4):
        arr[2][i] = mystr[idx]
        idx += 1
        diamond(i, arr, direct)

    for lst in arr:
        for i in range(size):
            print(lst[i], end='')
        print()