N, K = map(int, input().split())
lst = [[0, 0]]
for _ in range(N):
    lst.append(list(map(int, input().split())))

arr = [[0]*(K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        w, v = lst[i][0], lst[i][1]

        if j < w:
            arr[i][j] = arr[i - 1][j]
        else:
            arr[i][j] = max(arr[i - 1][j], v + arr[i - 1][j - w])

print(arr[N][K])
