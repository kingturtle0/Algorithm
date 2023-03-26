import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
visited = [0]*N
path = []

def dfs(level, start):
    if level == M:
        print(*path)
        return

    prev = 0
    for i in range(start, N):
        if visited[i] == 0 and prev != numbers[i]:
            prev = numbers[i]
            visited[i] = 1
            path.append(numbers[i])
            dfs(level + 1, i)
            visited[i] = 0
            path.pop()

dfs(0, 0)
