import sys
sys.setrecursionlimit(10000)

def dfs(level):
	if level == M:
		print(*path)
		return
	for i in range(N):
		if visited[i] == 0:
			visited[i] = 1
			path.append(i + 1)
			dfs(level + 1)
			visited[i] = 0
			path.pop()
            
N, M = map(int, input().split())
visited = [0]*N
path = []
dfs(0)