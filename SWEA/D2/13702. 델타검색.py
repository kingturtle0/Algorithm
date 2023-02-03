for test_case in range(1, 10):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    direct = [(-1,0),(0,-1),(0,1),(1,0)]

    def absSum(y, x):
        total = 0
        for i in range(4):
            dy = y + direct[i][0]
            dx = x + direct[i][1]

            if 0 <= dy < N and 0 <= dx < N:
                total += arr[dy][dx]-arr[y][x] if arr[dy][dx]-arr[y][x] > 0 else arr[y][x] - arr[dy][dx]

        return total

    result = 0
    for i in range(N):
        for j in range(N):
            result += absSum(i, j)

    print(f'#{test_case}', result)
