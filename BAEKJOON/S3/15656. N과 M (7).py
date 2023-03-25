N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
path = []

def dfs(level):
    if level == M:
        print(*path)
        return

    for i in range(N):
        path.append(numbers[i])
        dfs(level + 1)
        path.pop()

dfs(0)