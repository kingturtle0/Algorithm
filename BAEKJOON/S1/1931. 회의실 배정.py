import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))

lst.sort(key=lambda x:(x[1], x[0]))

ans = 1
ed = lst[0][1]
for i in range(1, N):
    if lst[i][0] >= ed:
        ed = lst[i][1]
        ans += 1

print(ans)