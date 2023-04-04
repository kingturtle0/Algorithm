def solve(n, st):
    if n == 6:
        print(*path)
        return

    for i in range(st, N):
        if v[i] == 0:
            v[i] = 1
            path.append(lst[i])
            solve(n + 1, i + 1)
            v[i] = 0
            path.pop()

while True:
    lst = list(map(int, input().split()))
    N = lst.pop(0)
    if N == 0:
        break

    path = []
    v = [0]*N
    solve(0, 0)
    print()