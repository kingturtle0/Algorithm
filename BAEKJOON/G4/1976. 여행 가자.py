import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
lst = list(range(N + 1))
arr = [list(map(int, input().split())) for _ in range(N)]
result = [0] + list(map(int, input().split()))


def Find(x):
    if x == lst[x]:
        return x
    else:
        lst[x] = Find(lst[x])
        return lst[x]


def Union(a, b):
    fa, fb = Find(a), Find(b)
    if fa == fb:
        return
    else:
        lst[fb] = fa


for i in range(N):
    for j in range(N):
        if arr[i][j]:
            Union(i+1, j+1)

flag = Find(result[1])
for i in range(2, M + 1):
    if flag != Find(result[i]):
        flag = 0
        print("NO")
        break

if flag:
    print("YES")