N = int(input())
lst = list(map(int, input().split()))

pn = [1] * 1001
pn[0] = 0
pn[1] = 0
for i in range(2, int(1001**0.5) + 1):
    if pn[i] == 1:
        for j in range(i + i, 1001, i):
            pn[j] = 0

ans = 0
for i in lst:
    if pn[i] == 1:
        ans += 1

print(ans)