T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    weights = sorted(list(map(int, input().split())), reverse=True)
    trucks = sorted(list(map(int, input().split())), reverse=True)

    ans = 0
    w = t = 0
    while w < N and t < M:
        if weights[w] <= trucks[t]:
            ans += weights[w]
            w += 1
            t += 1
        else:
            w += 1

    print(f'#{test_case}', ans)