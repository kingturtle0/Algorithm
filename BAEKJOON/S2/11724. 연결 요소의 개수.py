import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

visited = [0]*(N + 1)

def dfs(s):
    for num in arr[s]:
        if visited[num] == 0:
            visited[num] = 1
            dfs(num)

ans = 0
for i in range(1, N + 1):
    if visited[i] == 0:
        ans += 1
        dfs(i)

print(ans)