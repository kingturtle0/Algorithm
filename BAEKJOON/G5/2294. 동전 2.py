N, K = map(int, input().split())
coins = set([int(input()) for _ in range(N)])
INF = K + 1
dp = [INF] * (K + 1)
dp[0] = 0

for coin in coins:
    for j in range(1, K + 1):
        if j - coin >= 0:
            dp[j] = min(dp[j], dp[j - coin] + 1)

if dp[K] == INF:
    print(-1)
else:
    print(dp[K])