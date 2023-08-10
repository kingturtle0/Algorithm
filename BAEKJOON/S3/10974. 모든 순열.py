def dfs(n):
    if n == N:
        print(*path)
        return

    for i in range(N):
        if v[i] == 0:
            path.append(i + 1)
            v[i] = 1
            dfs(n + 1)
            path.pop()
            v[i] = 0

N = int(input())
path = []
v = [0]*N
dfs(0)