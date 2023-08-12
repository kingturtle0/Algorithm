from collections import deque
import sys


def bfs(si, sj):
    q = deque()
    q.append((si, sj))

    while q:
        ci, cj = q.popleft()

        for di, dj in d:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < h and 0 <= nj < w and arr[ni][nj] == 1 and v[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = 1


input = sys.stdin.readline


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(h)]
    v = [[0]*w for _ in range(h)]
    d = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

    ans = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and v[i][j] == 0:
                v[i][j] = 1
                bfs(i, j)
                ans += 1

    print(ans)
