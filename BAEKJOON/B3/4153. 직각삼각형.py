while True:
    a, b, c = map(int, input().split())

    if a == 0:
        break

    asqr = a ** 2
    bsqr = b ** 2
    csqr = c ** 2
    ans = "wrong"
    if (a >= b and a >= c and asqr == bsqr + csqr) or (b >= c and b >= a and bsqr == asqr + csqr) or (c >= a and c >= b and csqr == asqr + bsqr):
        ans = "right"

    print(ans)