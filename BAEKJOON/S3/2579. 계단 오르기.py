N = int(input())

lst = [0] + [int(input()) for _ in range(N)]
dp = [0]*(N + 1)

if N <= 3:
    ans = sum(lst)
else:
    dp[1] = lst[1]
    dp[2] = sum(lst[:3])
    for i in range(3, N + 1):
        dp[i] = max(lst[i] + lst[i - 1] + dp[i - 3], lst[i] + dp[i - 2])
    
    ans = dp[N]

print(ans)