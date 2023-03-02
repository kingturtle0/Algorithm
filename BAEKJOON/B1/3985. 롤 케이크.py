L = int(input())
N = int(input())
lst = [0]*(L+1)

ans1 = 0
max1 = 0
for i in range(1, N+1):
    P, K = map(int, input().split())
    if max1 < K - P:
        max1 = K - P
        ans1 = i

    for j in range(P, K+1):
        if lst[j] == 0:
            lst[j] = i

ans2 = 0
max2 = 0
for i in range(1, N + 1):
    cnt = lst.count(i)
    if max2 < cnt:
        max2 = cnt
        ans2 = i

print(ans1)
print(ans2)