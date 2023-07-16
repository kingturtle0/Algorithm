from collections import deque


def bfs(si, sj, color):
    q = deque()
    q.append((si, sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.popleft()

        for di, dj in d:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] in color and v[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = 1


N = int(input())
arr = [list(input()) for _ in range(N)]
d = ((-1, 0), (1, 0), (0, -1), (0, 1))
v = [[0 for _ in range(N)] for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == "R" and v[i][j] == 0:
            bfs(i, j, "R")
            ans += 1
        elif arr[i][j] == "G" and v[i][j] == 0:
            bfs(i, j, "G")
            ans += 1
        elif arr[i][j] == "B" and v[i][j] == 0:
            bfs(i, j, "B")
            ans += 1

ans2 = 0
v = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] in ["R", "G"] and v[i][j] == 0:
            bfs(i, j, ["R", "G"])
            ans2 += 1
        elif arr[i][j] == "B" and v[i][j] == 0:
            bfs(i, j, "B")
            ans2 += 1

print(ans, ans2)
