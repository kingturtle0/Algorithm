N = int(input())

ans = 0
if N % 2 == 0 and N > 1:
    dp = [0] * (N + 1)
    dp[2] = 3

    for i in range(4, N + 1, 2):
        dp[i] = dp[i - 2] * 3 + 2
        for j in range(i - 4, 1, -2):
            dp[i] += dp[j] * 2

    ans = dp[N]

print(ans)