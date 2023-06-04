from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


def bfs(si, sj, v):
    q = deque()
    q.append((si, sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.popleft()

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if arr[ni][nj] and not v[ni][nj]:
                q.append((ni, nj))
                v[ni][nj] = 1


def func():
    year = 1
    while True:
        q = deque()

        for i in range(1, N - 1):
            for j in range(1, M - 1):
                if arr[i][j]:
                    cnt = 0
                    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        ni, nj = i + di, j + dj
                        if not arr[ni][nj]:
                            cnt += 1
                    q.append((i, j, cnt))

        while q:
            ci, cj, cnt = q.popleft()
            if arr[ci][cj] > 0:
                arr[ci][cj] = max(0, arr[ci][cj] - cnt)

        v = [[0 for _ in range(M)] for _ in range(N)]
        flag = 0

        for i in range(1, N - 1):
            for j in range(1, M - 1):
                if arr[i][j] and not v[i][j]:
                    bfs(i, j, v)
                    flag += 1
                    if flag > 1:
                        return year

        if not flag:
            return 0

        year += 1


ans = func()
print(ans)