import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M, V = map(int, input().split())
arr = [[] for _ in range(N + 1)]
d_visited = [0] * (N + 1)
b_visited = [0] * (N + 1)
d_path = [V]
b_path = []

def dfs(n):
    if sum(d_visited) == N:
        return

    for num in sorted(arr[n]):
        if d_visited[num] == 0:
            d_visited[num] = 1
            d_path.append(num)
            dfs(num)

def bfs(n):
    q = [n]

    while q:
        c = q.pop(0)

        b_path.append(c)

        if len(b_path) == N:
            return

        for num in sorted(arr[c]):
            if b_visited[num] == 0:
                b_visited[num] = 1
                q.append(num)

for _ in range(M):
    i, j = map(int, input().split())
    arr[i].append(j)
    arr[j].append(i)

d_visited[V] = 1
b_visited[V] = 1
dfs(V)
bfs(V)

print(*d_path)
print(*b_path)