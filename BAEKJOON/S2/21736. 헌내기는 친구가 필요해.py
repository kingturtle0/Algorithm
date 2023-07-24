import sys
from collections import deque


def getij():
    for i in range(N):
        for j in range(M):
            if arr[i][j] == "I":
                return [i, j]


def bfs(si, sj):
    global ans
    q = deque()
    q.append((si, sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.popleft()

        if arr[ci][cj] == "P":
            ans += 1

        for di, dj in d:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and v[ni][nj] == 0 and arr[ni][nj] != "X":
                q.append((ni, nj))
                v[ni][nj] = 1


input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
v = [[0]*M for _ in range(N)]
d = ((-1, 0), (1, 0), (0, -1), (0, 1))

y, x = getij()
ans = 0
bfs(y, x)

if ans == 0:
    ans = "TT"

print(ans)