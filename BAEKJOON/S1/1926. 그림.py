from collections import deque

def bfs(si, sj):
    q = deque()
    q.append((si, sj))

    ret = 1
    while q:
        ci, cj = q.popleft()

        for di, dj in d:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < m and v[ni][nj] == 0 and arr[ni][nj] == 1:
                q.append((ni, nj))
                v[ni][nj] = 1
                ret += 1
    return ret

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
v = [[0]*m for _ in range(n)]
d = ((-1, 0), (1, 0), (0, -1), (0, 1))

cnt, ans = 0, 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and v[i][j] == 0:
            v[i][j] = 1
            ans = max(ans, bfs(i, j))
            cnt += 1

print(cnt, ans, sep='\n')