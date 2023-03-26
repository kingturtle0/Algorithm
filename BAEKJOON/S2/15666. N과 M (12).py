import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
path = []

def dfs(level, start):
    if level == M:
        print(*path)
        return

    prev = 0
    for i in range(start, N):
        if prev != numbers[i]:
            prev = numbers[i]
            path.append(numbers[i])
            dfs(level + 1, i)
            path.pop()

dfs(0, 0)
