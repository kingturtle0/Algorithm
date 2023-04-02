def backt(n, val):
    global mx, mn
    if n == N:
        mx = max(mx, val)
        mn = min(mn, val)
        return

    for i in range(4):
        if used[i]:
            if i == 0:
                used[i] -= 1
                backt(n + 1, val + lst[n])
                used[i] += 1
            elif i == 1:
                used[i] -= 1
                backt(n + 1, val - lst[n])
                used[i] += 1
            elif i == 2:
                used[i] -= 1
                backt(n + 1, val * lst[n])
                used[i] += 1
            else:
                used[i] -= 1
                backt(n + 1, int(val / lst[n]))
                used[i] += 1

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    used = list(map(int, input().split()))
    lst = list(map(int, input().split()))

    mx = -10e7
    mn = 10e7
    backt(1, lst[0])

    print(f'#{test_case} {mx - mn}')
