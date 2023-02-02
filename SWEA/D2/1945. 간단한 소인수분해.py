T = int(input())

for test_case in range(1, T + 1):
    num = int(input())
    a, b, c, d, e = 0, 0, 0, 0, 0
    while num != 1:
        if num % 2 == 0:
            num //= 2
            a += 1
        elif num % 3 == 0:
            num //= 3
            b += 1
        elif num % 5 == 0:
            num //= 5
            c += 1
        elif num % 7 == 0:
            num //= 7
            d += 1
        else:
            num //= 11
            e += 1
    print(f'#{test_case}', a, b, c, d, e)
# 위는 하나씩 다 쓴 코드

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    degree = [0] * 5
    numbers = [2, 3, 5, 7, 11]
    while N != 1:
        for i in range(5):
            if N % numbers[i] == 0:
                N //= numbers[i]
                degree[i] += 1

    a, b, c, d, e = degree
    print(f'#{test_case} {a} {b} {c} {d} {e}')
