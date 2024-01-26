def solution(n):
    primes = [0, 0] + [1] * (n - 1)
    for i in range(2, n + 1):
        if primes[i]:
            for j in range(i*2, n + 1, i):
                primes[j] = 0
    return sum(primes)