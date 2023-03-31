def dfs(n, sm):
    global ans
    if sm >= ans:
        return

    if n == N:
        ans = min(ans, sm)
        return

    for i in range(N):
        if v[i] == 0:
            v[i] = 1
            dfs(n + 1, sm + arr[n][i])
            v[i] = 0


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [0] * N

    ans = 10000
    dfs(0, 0)

    print(f'#{test_case} {ans}')