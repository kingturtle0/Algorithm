from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]


def bfs(si, sj, v):
    q = deque()

    q.append((si, sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.popleft()

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = 1

ans = 0
for h in range(0, 101):
    v = [[0 for _ in range(N)] for _ in range(N)]
    cnt, flag = 0, 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= h:
                v[i][j] = 1
                flag += 1

    if flag == N*N:
        break

    for i in range(N):
        for j in range(N):
            if v[i][j] == 0:
                bfs(i, j, v)
                cnt += 1

    ans = max(ans, cnt)

print(ans)