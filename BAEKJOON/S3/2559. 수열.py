N, K = map(int, input().split())
lst = list(map(int, input().split()))

ans = val = sum(lst[:K])
for i in range(K, N):
    val += lst[i]
    val -= lst[i-K]
    ans = max(val, ans)

print(ans)