T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    ans = N*M
    for i in range(N-2):
        for j in range(i+1, N-1):
            cnt = 0
            for k in range(i+1):
                cnt += M - arr[k].count('W')
            for k in range(i+1, j+1):
                cnt += M - arr[k].count('B')
            for k in range(j+1, N):
                cnt += M - arr[k].count('R')
            ans = min(cnt, ans)

    print(f'#{test_case}', ans)