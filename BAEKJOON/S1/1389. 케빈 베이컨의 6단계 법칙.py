from collections import deque
import sys
input = sys.stdin.readline


def bfs(s):
    q = deque()
    v = [0]*(N + 1)

    q.append(s)
    v[s] = 1

    while q:
        c = q.popleft()

        for n in arr[c]:
            if v[n] == 0:
                q.append(n)
                v[n] = v[c] + 1

    return sum(v)


N, M = map(int, input().split())
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    if b in arr[a]: continue
    arr[a].append(b)
    arr[b].append(a)


mn = 100
ans = 0
for i in range(1, N + 1):
    k = bfs(i)
    if k < mn:
        mn = k
        ans = i

print(ans)