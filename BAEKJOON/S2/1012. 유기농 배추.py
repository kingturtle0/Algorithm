from collections import deque
import sys

def bfs(y, x):
    q = deque()
    q.append((y, x))
    arr[y][x] = 0

    while q:
        cy, cx = q.popleft()

        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] == 1:
                q.append((ny, nx))
                arr[ny][nx] = 0


input = sys.stdin.readline

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        arr[Y][X] = 1

    ans = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                bfs(i, j)
                ans += 1

    print(ans)