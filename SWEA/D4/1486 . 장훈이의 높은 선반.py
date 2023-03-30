def dfs(start, val):
    global ans
    if val >= B:
        ans = min(ans, val)
        return

    for i in range(start, N):
        dfs(i + 1, val + heights[i])


T = int(input())

for test_case in range(1, T + 1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))

    ans = 10e8
    dfs(0, 0)
    print(f'#{test_case}', ans - B)