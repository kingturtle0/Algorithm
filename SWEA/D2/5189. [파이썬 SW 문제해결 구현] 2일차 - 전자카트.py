T = int(input())


def dfs(level):
    global ans
    if level == N - 1:
        val = 0
        for i in range(N):
            if i == N - 1:
                val += arr[path[i] - 1][0]
            else:
                val += arr[path[i] - 1][path[i + 1] - 1]
        ans = min(ans, val)
        return

    for i in range(2, N + 1):
        if visited[i] == 0:
            visited[i] = 1
            path.append(i)
            dfs(level + 1)
            visited[i] = 0
            path.pop()


for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N + 1)
    path = [1]

    ans = 10e8
    dfs(0)

    print(f'#{test_case}', ans)