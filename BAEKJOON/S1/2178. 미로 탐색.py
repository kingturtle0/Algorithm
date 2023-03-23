N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

def bfs(si, sj):
    q = [(si, sj)]
    visited[si][sj] = 1

    while q:
        ci, cj = q.pop(0)

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                visited[ni][nj] = visited[ci][cj] + 1
                q.append((ni, nj))

bfs(0, 0)
print(visited[N - 1][M - 1])