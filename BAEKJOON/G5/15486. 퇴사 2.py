import sys
input = sys.stdin.readline

N = int(input())
arr = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]

result = [0] * (N + 1)
for t in range(1, N + 1):
    T, P = arr[t]
    result[t] = max(result[t - 1], result[t])
    if t + T <= N + 1:
        result[t + T - 1] = max(result[t + T - 1], P + result[t - 1])

print(result[N])
