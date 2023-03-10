import sys
input = sys.stdin.readline

N = int(input())
lst = [(int(input()), i) for i in range(N)]
lst.sort()

ans = 0
for i in range(N):
    ans = max(ans, lst[i][1] - i)

print(ans + 1)