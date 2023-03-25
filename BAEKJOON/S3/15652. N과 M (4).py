N, M = map(int, input().split())
path = []

def dfs(level, start):
    if level == M:
        print(*path)
        return

    for i in range(start, N):
        path.append(i + 1)
        dfs(level + 1, i)
        path.pop()

dfs(0, 0)
