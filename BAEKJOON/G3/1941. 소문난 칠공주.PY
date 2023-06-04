from collections import deque

arr = [input() for _ in range(5)]
ans = 0
dv = [[0 for _ in range(5)] for _ in range(5)]


def bfs(si, sj):
    q = deque()
    bv = [[0 for _ in range(5)] for _ in range(5)]

    q.append((si, sj))
    bv[si][sj] = 1

    cnt = 0
    while q:
        ci, cj = q.popleft()
        cnt += 1

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < 5 and 0 <= nj < 5 and dv[ni][nj] and bv[ni][nj] == 0:
                q.append((ni, nj))
                bv[ni][nj] = 1

    return cnt == 7


def check():
    for i in range(5):
        for j in range(5):
            if dv[i][j]:
                return bfs(i, j)


def dfs(n, cnt, y):
    global ans
    if y > 3 or cnt > 7:
        return

    if n == 25:
        if cnt == 7 and check():
            ans += 1
        return

    dv[n//5][n%5] = 1
    dfs(n + 1, cnt + 1, y + int(arr[n//5][n%5] == "Y"))
    dv[n//5][n%5] = 0
    dfs(n + 1, cnt, y)

dfs(0, 0, 0)

print(ans)