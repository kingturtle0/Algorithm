def check():
    for dr, dc in direct:
        nnr, nnc = r + dr, c + dc
        if arr[nnr][nnc] == 0:
            return True
    return False


N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

direct = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ans = 0
while True:
    if arr[r][c] == 0:
        arr[r][c] = 2
        ans += 1

    if check():
        d = (d + 3) % 4
        nr, nc = r + direct[d][0], c + direct[d][1]
        if arr[nr][nc] == 0:
            r, c = nr, nc
    else:
        nr, nc = r - direct[d][0], c - direct[d][1]
        if arr[nr][nc] == 1:
            break
        else:
            r, c = nr, nc

print(ans)
