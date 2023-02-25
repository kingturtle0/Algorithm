def bfs(si, sj):
    q = []
    q.append([si, sj])
    v[si][sj] = 1

    while q:
        ci, cj = q.pop(0)

        for di, dj in ((-1,0), (1,0), (0,-1), (0,1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < 16 and 0 <= nj < 16 and arr[ni][nj] != 1 and v[ni][nj] == 0:
                q.append([ni, nj])
                v[ni][nj] = 1
                if arr[ni][nj] == 3:
                    return 1

    return 0

T = 10
for test_case in range(10):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    v = [[0]*16 for _ in range(16)]

    si, sj = 0, 0
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                si, sj = i, j
                break

    ans = bfs(si, sj)

    print(f'#{n}', ans)