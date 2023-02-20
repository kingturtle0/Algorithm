T = int(input())

def isGoal(sy, sx):
    global flag
    if arr[sy][sx] == '3':
        flag = 1
        return

    for dy, dx in [(-1,0), (1,0), (0,-1), (0,1)]:
        gy = sy + dy
        gx = sx + dx
        if 0 <= gy < N and 0 <= gx < N:
            if arr[gy][gx] != '1' and visited[gy][gx] == 0:
                visited[gy][gx] = 1
                isGoal(gy, gx)

for test_case in range(1, T + 1):
    N = int(input())
    arr = [input() for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    flag = 0

    sy, sx = 0, 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                sy, sx = i, j
                break

    visited[sy][sx] = 1
    isGoal(sy, sx)
    if flag:
        ans = 1
    else:
        ans = 0

    print(f'#{test_case}', ans)