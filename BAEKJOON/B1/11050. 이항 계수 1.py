N, K = map(int, input().split())

n = 1
for i in range(2, N + 1):
    n *= i

k = 1
if K > 0:
    for i in range(2, K + 1):
        k *= i

nk = 1
if N - K > 0:
    for i in range(2, N - K + 1):
        nk *= i

print(n//(k*nk))