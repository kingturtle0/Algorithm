import sys
input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]
ans = 1
prev = lst[-1]
for i in range(N - 1, -1, -1):
    if lst[i] > prev:
        prev = lst[i]
        ans += 1

print(ans)