N, K = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(int(input()))

ans = 0
for i in range(N - 1, -1, -1):
    if K >= lst[i]:
        ans += K//lst[i]
        K %= lst[i]
    

print(ans)