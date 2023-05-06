N = int(input())
arr = [[0]*12 for _ in range(N + 1)]
arr[1][2:11] = [1]*9

for i in range(2, N + 1):
    for j in range(1, 11):
        arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j + 1]

print(sum(arr[N])%(int(1e9)))