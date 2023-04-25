from collections import deque
import sys

input = sys.stdin.readline

N, M, K, X = map(int, input().split())
arr = [[] for _ in range(N + 1)]
v = [0]*(N + 1)
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)

def bfs(start):
    q = deque()
    q.append(start)
    v[start] = 1

    while q:
        c = q.popleft()

        for n in arr[c]:
            if v[n] == 0:
                v[n] = v[c] + 1
                q.append(n)

bfs(X)

flag = 1
for i in range(N + 1):
    if v[i] - 1 == K:
        flag = 0
        print(i)

if flag:
    print(-1)