N, M = map(int, input().split())

def gcd(n, m):
    while m:
        n, m = m, n % m
    return n

if N < M:
    a = gcd(M, N)
else:
    a = gcd(N, M)

print(a)
print(N*M//a)