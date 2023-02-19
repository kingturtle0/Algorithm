T = int(input())

def dfs(row, val):
    global ans
    if ans <= val:
        return

    if row == N - 1:
        if ans > val:
            ans = val
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(row + 1, val + arr[row+1][i])
            visited[i] = 0

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 21e8

    for i in range(N):
        visited = [0] * N
        visited[i] = 1
        dfs(0, arr[0][i])

    print(f'#{test_case}', ans)