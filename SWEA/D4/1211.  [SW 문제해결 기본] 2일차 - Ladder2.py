T = 10

for test_case in range(1, T + 1):
    tc = int(input())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    min_val = 21e8

    for sj in range(1, 101):
        si = 0
        if arr[si][sj] != 1:
            continue

        dj, cnt = 0, 0
        ci, cj = si, sj
        while ci < 99:
            cnt += 1
            if dj == 0:
                if arr[ci][cj+1] == 1:
                    dj = 1
                    cj += 1
                elif arr[ci][cj-1] == 1:
                    dj = -1
                    cj -= 1
                else:
                    ci += 1
            else:
                if arr[ci][cj+dj] == 1:
                    cj += dj
                else:
                    dj = 0
                    ci += 1

            cnt += 1

        if min_val >= cnt:
            min_val = cnt
            idx = sj - 1

    print(f'#{tc}', idx)