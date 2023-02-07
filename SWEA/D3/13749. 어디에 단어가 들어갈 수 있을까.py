T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt_r = cnt_c = 0
    result = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                cnt_r += 1
            else:
                if cnt_r == K:
                    result += 1
                cnt_r = 0

            if arr[j][i]:
                cnt_c += 1
            else:
                if cnt_c == K:
                    result += 1
                cnt_c = 0

        if cnt_r == K:
            result += 1
        cnt_r = 0

        if cnt_c == K:
            result += 1
        cnt_c = 0

    print(f'#{test_case}', result)