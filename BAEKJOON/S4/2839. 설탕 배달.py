N = int(input())

def func(a, b, n):
    cnt = 0
    while True:
        if n % b == 0:
            cnt += n // b
            return cnt
        n -= a
        cnt += 1

        if n < 0:
            cnt = -1
            return cnt

ans = min(func(5, 3, N), func(3, 5, N))
print(ans)