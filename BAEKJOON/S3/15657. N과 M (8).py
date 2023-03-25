N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
path = []

def dfs(level, start):
    if level == M:
        print(*path)
        return

    for i in range(start, N):
        path.append(numbers[i])
        dfs(level + 1, i)
        path.pop()

dfs(0, 0)