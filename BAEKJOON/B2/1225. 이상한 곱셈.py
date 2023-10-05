A, B = input().split()
ans = 0
sum_b = sum(map(int, B))
for a in A:
    ans += int(a)*sum_b
print(ans)