import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

N, M = map(int, input().split())
arr = list(range(N + 1))


def Find(x):
    if x == arr[x]:
        return x
    else:
        arr[x] = Find(arr[x])
        return arr[x]


def Union(a, b):
    fa, fb = Find(a), Find(b)
    if fa == fb:
        return
    else:
        arr[fb] = fa


for _ in range(M):
    check, a, b = map(int, input().split())
    if check:
        if Find(a) == Find(b):
            print('YES')
        else:
            print('NO')
    else:
        Union(a, b)