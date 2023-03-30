def dfs(level, val):
    global answer
    if val > K:
        return

    if val == K:
        answer += 1
        return

    if level == N:
        return

    dfs(level + 1, val + numbers[level])
    dfs(level + 1, val)


T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))

    answer = 0
    dfs(0, 0)

    print(f'#{test_case}', answer)