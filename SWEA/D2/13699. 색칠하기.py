T = int(input())

for test_case in range(1, T + 1):
    arr = [[0] * 10 for _ in range(10)]

    def Coloring(y1, x1, y2, x2, c):
        for i in range(y1, y2+1):
            for j in range(x1, x2+1):
                arr[i][j] += c

    N = int(input())
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        Coloring(r1, c1, r2, c2, color)

    cnt = 0
    for lst in arr:
        for elem in lst:
            if elem == 3:
                cnt += 1

    print(f'#{test_case}', cnt)