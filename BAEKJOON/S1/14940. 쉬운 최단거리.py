from collections import deque
import sys
input = sys.stdin.readline


def bfs(si, sj):
    q = deque()
    q.append((si, sj))

    while q:
        ci, cj = q.popleft()

        for di, dj in d:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 1 and v[ni][nj] == 0:
                v[ni][nj] = v[ci][cj] + 1
                q.append((ni, nj))


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
v = [[0]*m for _ in range(n)]
d = ((-1, 0), (1, 0), (0, -1), (0, 1))

flag = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            flag = 1
            v[i][j] = 1
            bfs(i, j)
            break
    if flag:
        break

for i in range(n):
    for j in range(m):
        if arr[i][j] != 0 and v[i][j] != 0:
            ans = v[i][j] - 1
        elif arr[i][j] == 0 and v[i][j] == 0:
            ans = 0
        else:
            ans = -1
        print(ans, end=' ')
    print()