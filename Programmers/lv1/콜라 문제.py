def solution(a, b, n):
    answer = 0
    while n >= a:
        d, r = n // a * b, n % a
        answer += d
        n = d + r
    return answer