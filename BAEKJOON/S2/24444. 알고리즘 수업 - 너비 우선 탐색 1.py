import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    q = deque()
    visited[start] = 1
    q.append(start)
    cnt = 1

    while q:
        next = q.popleft()
        for end in sorted(graph[next]):
            if visited[end] == 0:
                cnt += 1
                q.append(end)
                visited[end] = cnt

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [0] * (N + 1)

bfs(R)
print(*visited[1:], sep='\n')