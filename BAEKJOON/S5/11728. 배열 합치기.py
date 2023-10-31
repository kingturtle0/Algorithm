import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = []
n, m = 0, 0
while True:
    if A[n] > B[m]:
        result.append(B[m])
        m += 1
    else:
        result.append(A[n])
        n += 1
    
    if n == N:
        while m < M:
            result.append(B[m])
            m += 1
        break
    elif m == M:
        while n < N:
            result.append(A[n])
            n += 1
        break

print(*result)