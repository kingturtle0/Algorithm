import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr1, arr2 = [], []

for _ in range(M):
    y, x = map(int, input().split())
    arr1.append(y)
    arr2.append(x)

arr1.sort()
arr2.sort()

m1 = arr1[M//2]
m2 = arr2[M//2]

ans = 0
for i in range(M):
    ans += abs(m1-arr1[i]) + abs(m2-arr2[i])

print(ans)