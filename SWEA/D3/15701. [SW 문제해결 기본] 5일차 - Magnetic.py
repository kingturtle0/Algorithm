T = 10
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for j in range(N):
        val = 0
        for i in range(N):
            if arr[i][j] != 0:
                if arr[i][j] == 2 and val == 1:
                    ans += 1
                val = arr[i][j]

    print(f'#{test_case}', ans)