def solution(brown, yellow):
    n = brown + yellow
    for i in range(int(n ** 0.5), 0, -1):
        if n % i == 0 and (i - 2) * (n // i - 2) == yellow:
            return [n // i, i]