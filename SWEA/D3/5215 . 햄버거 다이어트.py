def dfs(n, score, kcal):
    global ans
    if kcal > L:
        return

    if n == N:
        ans = max(ans, score)
        return

    dfs(n + 1, score, kcal)
    dfs(n + 1, score + arr[n][0], kcal + arr[n][1])


T = int(input())

for test_case in range(1, T + 1):
    N, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    dfs(0, 0, 0)
    print(f'#{test_case} {ans}')