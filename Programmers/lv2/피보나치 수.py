def solution(n):
    # fibos = [0, 1] + [0] * (n - 1)
    # for i in range(2, n + 1):
    #     fibos[i] = fibos[i - 1] + fibos[i - 2]
    # return fibos[n] % 1234567
    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, a + b
    return b % 1234567