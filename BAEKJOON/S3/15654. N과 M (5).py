N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
visited = [0]*N
path = []

def dfs(level):
    if level == M:
        print(*path)
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            path.append(numbers[i])
            dfs(level + 1)
            path.pop()
            visited[i] = 0

dfs(0)