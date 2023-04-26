import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
A = [[] for _ in range(N + 1)]
answer = [0] * (N + 1)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_node = queue.popleft()
        for i in A[now_node]:
            if not visited[i]:
                visited[i] = True
                answer[i] += 1
                queue.append(i)

for _ in range(M):
    S, E = map(int, input().split())
    A[S].append(E)

for i in range(1, N + 1):
    visited = [False] * (N + 1)
    BFS(i)

mx = 0
for i in range(1, N + 1):
    mx = max(mx, answer[i])

for i in range(1, N + 1):
    if mx == answer[i]:
        print(i, end=' ')