import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[] for _ in range(N)]
visited = [0]*N
ans = 0

def dfs(level, n):
    global ans
    if level == 4:
        ans = 1
        return

    visited[n] = 1
    for num in arr[n]:
        if visited[num] == 0:
            dfs(level + 1, num)
    visited[n] = 0


for _ in range(M):
    i, j = map(int, input().split())
    arr[i].append(j)
    arr[j].append(i)

for i in range(N):
    dfs(0, i)
    if ans:
        break

print(ans)