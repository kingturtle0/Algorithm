N = int(input())
for _ in range(N):
    A, B = map(int, input().split())

    a = max(A, B)
    b = min(A, B)
    remainder = 1
    while remainder:
        remainder = a % b
        a = b
        b = remainder

    gcd = a
    print(A*B//gcd)