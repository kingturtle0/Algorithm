for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    ans = ''
    if p1 < x2 or p2 < x1 or q2 < y1 or q1 < y2:
        ans = "d"
    elif y1 == q2 or y2 == q1:
        if x2 == p1 or x1 == p2:
            ans = "c"
        else:
            ans = "b"
    elif p1 == x2 or p2 == x1:
        if q1 == y2 or q2 == y1:
            ans = "c"
        else:
            ans = "b"
    else:
        ans = "a"

    print(ans)