def dfs(n, cnt):
    global ans
    if ans <= cnt:
        return

    if n >= N:
        ans = min(ans, cnt)
        return

    for i in range(lst[n], 0, -1):
        dfs(n + i, cnt + 1)


T = int(input())

for test_case in range(1, T + 1):
    lst = list(map(int, input().split()))
    N = lst[0]

    ans = 1000
    dfs(1, -1)

    print(f'#{test_case} {ans}')