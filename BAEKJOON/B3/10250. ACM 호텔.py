T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())

    f, b = 1, 1
    while N > 1:
        f += 1
        if f > H:
            f = 1
            b += 1

        N -= 1

    b = "0" + str(b) if b < 10 else str(b)
    print(str(f) + b)