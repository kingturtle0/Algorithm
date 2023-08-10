E, S, M = map(int, input().split())

ans = 0
e, s, m = 0, 0, 0
while True:
    e += 1
    s += 1
    m += 1
    ans += 1
    if e > 15:
        e = 1
    if s > 28:
        s = 1
    if m > 19:
        m = 1

    if e == E and s == S and m == M:
        print(ans)
        break