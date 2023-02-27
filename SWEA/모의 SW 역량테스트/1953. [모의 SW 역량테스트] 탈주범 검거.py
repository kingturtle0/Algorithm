p = [[], [0, 1, 2, 3], [0, 1], [2, 3], [0, 3], [1, 3], [1, 2], [0, 2]]
directi = [-1, 1, 0, 0]
directj = [0, 0, -1, 1]
opp = {0: 1, 1: 0, 2: 3, 3: 2}

def bfs(si, sj, L):
    q = []
    visited = [[0]*M for _ in range(N)]

    q.append((si, sj))
    visited[si][sj] = 1
    cnt = 1

    while q:
        ci, cj = q.pop(0)

        if visited[ci][cj] == L:
            return cnt

        for dr in p[arr[ci][cj]]:
            ni, nj = ci + directi[dr], cj + directj[dr]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and (opp[dr] in p[arr[ni][nj]]):
                q.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1
                cnt += 1

    return cnt

T = int(input())
for test_case in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = bfs(R, C, L)

    print(f'#{test_case}', ans)