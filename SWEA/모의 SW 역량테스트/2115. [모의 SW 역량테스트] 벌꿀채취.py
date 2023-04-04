def backt(lst, m, ret, val, limit, v):
    ret = max(ret, val)
    if m == M:
        return ret

    if lst[m] > limit:
        return ret

    for i in range(2):
        if v[m] == 0:
            v[m] = 1
            ret = backt(lst, m + 1, ret, val + (lst[m]*lst[m]*i), limit - lst[m]*i, v)
            v[m] = 0

    return ret


def check(y, x):
    lst = [arr[y][x + i] for i in range(M)]
    if 0 in lst:
        return 0

    v = [0]*M
    ret = backt(lst, 0, 0, 0, C, v)
    return ret


T = int(input())

for test_case in range(1, T + 1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for _ in range(2):
        mx, zi, zj = 0, 0, 0
        for i in range(N):
            for j in range(N - M + 1):
                temp = check(i, j)
                if temp > mx:
                    mx = temp
                    zi, zj = i, j

        ans += mx
        for k in range(zj, zj + M):
            arr[zi][k] = 0

    print(f'#{test_case} {ans}')