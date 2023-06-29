from collections import deque
import sys

def bfs(i, j):
    q = deque()
    q.append((i, j))
    v[i][j] = 1
    cnt = 0

    while q:
        ci, cj = q.popleft()
        cnt += 1

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1 and v[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = 1

    return cnt

input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = [[0 for _ in range(M)] for _ in range(N)]
v = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    arr[r - 1][c - 1] = 1

ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and v[i][j] == 0:
            ans = max(ans, bfs(i, j))

print(ans)
