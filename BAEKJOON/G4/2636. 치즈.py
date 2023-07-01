from collections import deque
import sys


def bfs():
    q = deque()
    v = [[0 for _ in range(M)] for _ in range(N)]

    q.append((0, 0))
    v[0][0] = 1

    while q:
        ci, cj = q.popleft()

        for di, dj in direct:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and v[ni][nj] == 0 and arr[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = 1
                zeros.add((ni, nj))


def melt():
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                for di, dj in direct:
                    ni, nj = i + di, j + dj
                    if arr[ni][nj] == 0 and (ni, nj) in zeros:
                        arr[i][j] = 0
                        break


def check():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1

    return cnt


input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
direct = ((-1, 0), (1, 0), (0, -1), (0, 1))
zeros = set()

time = 0
ans = check()
while True:
    bfs()
    melt()
    time += 1
    if check():
        ans = check()
    else:
        break

print(time)
print(ans)
