from collections import deque

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

def bfs(si, sj):
    q = deque()
    q.append((si, sj))

    cnt = 0
    while q:
        ci, cj = q.popleft()
        arr[ci][cj] = 0
        cnt += 1

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj]:
                q.append((ni, nj))
                arr[ni][nj] = 0

    return cnt

results = []
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            results.append(bfs(i, j))

results.sort()
print(len(results))
for result in results:
    print(result)