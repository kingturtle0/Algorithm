from collections import deque
import sys
input = sys.stdin.readline

def bfs(snode, sedge):
    q = deque()
    visited = [0] * (V + 1)
    d = [0] * (V + 1)

    q.append((snode, sedge))
    visited[snode] = 1

    while q:
        cnode, cedge = q.popleft()

        for nnode, nedge in arr[cnode]:
            if visited[nnode] == 0:
                visited[nnode] = 1
                d[nnode] = d[cnode] + nedge
                q.append((nnode, nedge))

    return d


V = int(input())
arr = [[] for _ in range(V + 1)]
for _ in range(V):
    lst = list(map(int, input().split()))
    n = lst[0]
    idx = 1
    while True:
        if lst[idx] == -1:
            break
        arr[n].append((lst[idx], lst[idx + 1]))
        idx += 2



distance = bfs(1, 0)

mx = 0
st = 0
for i in range(V + 1):
    if mx < distance[i]:
        mx = distance[i]
        st = i

result = bfs(st, 0)
print(max(result))