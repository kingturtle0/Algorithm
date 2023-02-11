T = int(input())

def spray(arr, y, x, n, m):
    total1 = total2 = arr[y][x]
    direct1 = [[-1,0],[1,0],[0,-1],[0,1]]
    direct2 = [[-1,-1],[-1,1],[1,-1],[1,1]]

    for i in range(4):
        for j in range(1, m):
            dy1 = y + direct1[i][0]*j
            dx1 = x + direct1[i][1]*j
            if 0 <= dy1 < n and 0 <= dx1 < n:
                total1 += arr[dy1][dx1]

            dy2 = y + direct2[i][0]*j
            dx2 = x + direct2[i][1]*j
            if 0 <= dy2 < n and 0 <= dx2 < n:
                total2 += arr[dy2][dx2]

    if total1 > total2:
        return total1
    else:
        return total2

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_val = -(21e8)
    for i in range(n):
        for j in range(n):
            ret = spray(arr, i, j, n, m)
            if max_val < ret:
                max_val = ret

    print(f'#{test_case}', max_val)