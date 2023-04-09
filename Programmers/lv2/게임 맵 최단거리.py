from collections import deque

def solution(maps):
    def bfs(si, sj):
        q = deque()
        v = [[0] * m for _ in range(n)]

        q.append((si, sj))
        v[si][sj] = 1

        while q:
            ci, cj = q.popleft()


            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ni, nj = ci + di, cj + dj
                if 0 <= ni < n and 0 <= nj < m and v[ni][nj] == 0 and maps[ni][nj] != 0:
                    v[ni][nj] = v[ci][cj] + 1
                    q.append((ni, nj))

        return v[n - 1][m - 1]
    
    n = len(maps)
    m = len(maps[0])
    answer = bfs(0, 0)
    
    if answer:
        return answer
    else:
        return -1