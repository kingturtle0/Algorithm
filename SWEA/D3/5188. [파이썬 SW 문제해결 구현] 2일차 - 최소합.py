T = int(input())


def dfs(si, sj, val):
    global ans
    if si == N - 1 and sj == N - 1:
        ans = min(ans, val)
        return

    for di, dj in ((0, 1), (1, 0)):
        ni, nj = si + di, sj + dj
        if 0 <= ni < N and 0 <= nj < N:
            dfs(ni, nj, val + arr[ni][nj])



for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    ans = 10e8
    dfs(0, 0, arr[0][0])

    print(f'#{test_case}', ans)