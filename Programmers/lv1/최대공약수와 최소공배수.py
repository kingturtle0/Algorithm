def getgcd(n, m):
    n, m= min(n, m), max(n, m)
    while n != 0:
        n, m = m % n, n
    return m

def solution(n, m):
    gcd = getgcd(n, m)
    return [gcd, n * m // gcd]

# def solution(n, m):
#     d, r = min(n, m), max(n, m)
#     while d != 0:
#         d, r = r % d, d
#     return [r, n * m // r]