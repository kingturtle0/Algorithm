def dfs(n):
    global ans
    if n == N:
        if len(path) > 0 and sum(path) == S:
            ans += 1
        return

    for i in range(2):
        if i:
            path.append(lst[n])
            dfs(n + 1)
            path.pop()
        else:
            dfs(n + 1)

N, S = map(int, input().split())
lst = list(map(int, input().split()))
path = []

ans = 0
dfs(0)

print(ans)