from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[] for _ in range(N + 1)]
prior = [0]*(N + 1)
v = [0]*(N + 1)
q = deque()
for i in range(M):
    a, b = map(int, input().split())
    prior[b] += 1
    arr[a].append(b)


for i in range(1, N + 1):
    if prior[i] == 0:
        v[i] = 1
        q.append(i)


while q:
    c = q.popleft()
    print(c, end=' ')

    for i in arr[c]:
        if v[i] == 0:
            if prior[i] == 1:
                v[i] = 1
                prior[i] -= 1
                q.append(i)
            else:
                prior[i] -= 1