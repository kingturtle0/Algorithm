N = int(input())
num = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
y = x = d = 0
start = N ** 2
arr[y][x] = start
ans_y, ans_x = 1, 1

for n in range(start - 1, 0, -1):
    ny, nx = y + dy[d], x + dx[d]
    if not (0 <= ny < N and 0 <= nx < N and not arr[ny][nx]):
        d = (d + 1) % 4
        ny, nx = y + dy[d], x + dx[d]

    arr[ny][nx] = n
    y, x = ny, nx
    if n == num:
        ans_y, ans_x = y + 1, x + 1


for i in range(N):
    print(*arr[i])
print(ans_y, ans_x)
