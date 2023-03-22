import sys

sys.setrecursionlimit(10000)


def is_prime(number):
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


N = int(input())


def dfs(level, val):
    if level == N:
        print(val)
        return

    if level == 0:
        for n in ('2', '3', '5', '7'):
            dfs(level + 1, n)
    else:
        for n in range(1, 10, 2):
            num = val + str(n)
            if is_prime(int(num)):
                dfs(level + 1, num)


dfs(0, 0)
