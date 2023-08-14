def dfs(ci, cj, cnt):
    global ans
    ans = max(cnt, ans)

    for di, dj in d:
        ni, nj = ci + di, cj + dj
        if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] not in path:
            path.add(arr[ni][nj])
            dfs(ni, nj, cnt + 1)
            path.remove(arr[ni][nj])


R, C = map(int, input().split())

arr = [list(input()) for _ in range(R)]
path = set(arr[0][0])
d = ((-1, 0), (1, 0), (0, -1), (0, 1))

ans = 1
dfs(0, 0, 1)
print(ans)