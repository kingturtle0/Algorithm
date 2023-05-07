import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = [[0 for _ in range(N)] for _ in range(N)]

result[0][0] = 1

for i in range(N):
    for j in range(N):
        if result[i][j] > 0 and arr[i][j] > 0:
            n = arr[i][j]
            if j + n < N:
                result[i][j + n] += result[i][j]

            if i + n < N:
                result[i + n][j] += result[i][j]

print(result[N - 1][N - 1])