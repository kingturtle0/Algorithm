N, M = map(int, input().split())
k, *lst = map(int, input().split())
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


results = []
for _ in range(M):
    t, *tlst = map(int, input().split())
    results.append(tlst)

    for i in range(1, t):
        Union(tlst[0], tlst[i])

ans = 0
for result in results:
    for i in range(k):
        if Find(result[0]) == Find(lst[i]):
            break
    else:
        ans += 1

print(ans)