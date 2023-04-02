def backt(n, val):
    global ans
    if val >= ans:
        return

    if n >= 12:
        ans = min(ans, val)
        return

    backt(n + 1, val + lst[n] * d)
    backt(n + 1, val + m)
    backt(n + 3, val + q)
    backt(n + 12, val + y)


T = int(input())

for test_case in range(1, T + 1):
    d, m, q, y = map(int, input().split())
    lst = list(map(int, input().split()))

    ans = 3000 * 365
    backt(0, 0)
    print(f'#{test_case} {ans}')