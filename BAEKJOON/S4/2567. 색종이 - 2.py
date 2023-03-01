arr = [[0]*102 for _ in range(102)]

N = int(input())

for _ in range(N):
    y, x = map(int, input().split())
    for j in range(x, x+10):
        for i in range(y, y+10):
            arr[i][j] = 1

cnt = 0
for si in range(102):
    for sj in range(102):
        for di, dj in ((-1,0), (1,0), (0,-1), (0,1)):
            ni, nj = si + di, sj + dj
            if arr[si][sj] == 1 and arr[ni][nj] == 0:
                cnt += 1

print(cnt)