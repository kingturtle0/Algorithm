def bfs(si, sj):
    q = []
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    k = 0
    ret = 0

    q.append((si, sj))
    visited[si][sj] = 1
    cnt += arr[si][sj]

    while q:
        ci, cj = q.pop(0)

        if k != visited[ci][cj]:
            k = visited[ci][cj]
            if lst[k] <= cnt*M:
                if ret < cnt:
                    ret = cnt

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj

            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1
                cnt += arr[ni][nj]

    return ret


T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    lst = [k * k + (k - 1) * (k - 1) for k in range(N * 2)]

    ans = 0
    for i in range(N):
        for j in range(N):
            val = bfs(i, j)
            if ans < val:
                ans = val

    print(f'#{test_case}', ans)