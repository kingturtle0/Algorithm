N, M = map(int, input().split())
lst = list(map(int, input().split()))

prefix = [0]
temp = 0
for i in range(N):
    temp += lst[i]
    prefix.append(temp)

for j in range(M):
    a, b = map(int, input().split())
    ans = prefix[b] - prefix[a-1]
    print(ans)