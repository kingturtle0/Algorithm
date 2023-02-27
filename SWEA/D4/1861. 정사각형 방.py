def bfs(si, sj):
    q = []
    answers = []

    q.append((si, sj))
    visited[si][sj] = 1
    answers.append(arr[si][sj])

    while q:
        ci, cj = q.pop(0)

        for di, dj in ((-1,0), (1,0), (0,-1), (0,1)):
            ni, nj = ci + di, cj + dj

            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and abs(arr[ni][nj] - arr[ci][cj]) == 1:
                q.append((ni, nj))
                visited[ni][nj] = 1
                answers.append(arr[ni][nj])

    return min(answers), len(answers)

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    ans, ans_cnt = N*N, 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                tans, tans_cnt = bfs(i, j)
                if ans_cnt < tans_cnt or (ans_cnt == tans_cnt and ans > tans):
                    ans, ans_cnt = tans, tans_cnt

    print(f'#{test_case}', ans, ans_cnt)