from collections import deque


def copyarr(ar):
    newarr = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            newarr[i][j] = ar[i][j]
    return newarr


def bfs():
    narr = copyarr(arr)
    q = deque()
    v = [[0 for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if narr[i][j] == 2:
                q.append((i, j))

    while q:
        ci, cj = q.popleft()

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and narr[ni][nj] == 0 and v[ni][nj] == 0:
                q.append((ni, nj))
                narr[ni][nj] = 2
                v[ni][nj] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if narr[i][j] == 0:
                cnt += 1

    return cnt


def dfs(level):
    global ans
    if level == 3:
        ans = max(ans, bfs())
        return

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                dfs(level + 1)
                arr[i][j] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
dfs(0)
print(ans)
