from collections import deque
import sys

input = sys.stdin.readline

M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]


def bfs():
    q = deque()
    v = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]

    cnt = 0
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if arr[h][i][j] == 1:
                    q.append((h, i, j))
                    v[h][i][j] = 1
                elif arr[h][i][j] == 0:
                    cnt += 1

    while q:
        ch, ci, cj = q.popleft()

        for dh, di, dj in ((1, 0, 0), (-1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)):
            nh, ni, nj = ch + dh, ci + di, cj + dj
            if 0 <= nh < H and 0 <= ni < N and 0 <= nj < M and not arr[nh][ni][nj] and not v[nh][ni][nj]:
                q.append((nh, ni, nj))
                v[nh][ni][nj] = v[ch][ci][cj] + 1
                cnt -= 1

    if not cnt:
        return v[ch][ci][cj] - 1
    else:
        return -1


ans = bfs()
print(ans)