N = int(input())
M = int(input())
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    i, j = map(int, input().split())
    arr[i].append(j)
    arr[j].append(i)
visited = [0]*(N + 1)


def dfs(idx):
    for num in arr[idx]:
        if visited[num] == 0:
            visited[num] = 1
            dfs(num)

visited[1] = 1
dfs(1)

print(sum(visited) - 1)