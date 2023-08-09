N = int(input())
lst = [1]*1001

for i in range(100, 1001):
    x = str(i)
    prev = int(x[1]) - int(x[0])
    for j in range(2, len(x)):
        n = int(x[j]) - int(x[j - 1])
        if prev != n:
            lst[i] = 0
            break

ans = 0
for i in range(1, N + 1):
    if lst[i]:
        ans += 1

print(ans)