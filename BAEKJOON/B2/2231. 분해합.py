N = int(input())

ans = 0
for i in range(N):
    if N == (i + sum(map(int, str(i)))):
        ans = i
        break

print(ans)