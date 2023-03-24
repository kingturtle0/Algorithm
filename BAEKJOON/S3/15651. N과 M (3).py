import sys
sys.setrecursionlimit(10000)

def dfs(level):
    if level == M:
        print(*path)
        return
    
    for i in range(N):
        path.append(i + 1)
        dfs(level + 1)
        path.pop()
        
N, M = map(int, input().split())
path = []

dfs(0)