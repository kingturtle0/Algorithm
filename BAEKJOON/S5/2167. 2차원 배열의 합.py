import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
K = int(input())

# for _ in range(K):
#     i, j, x, y = map(int, input().split())
#     ans = 0
#     for ni in range(i - 1, x):
        
#         for nj in range(j - 1, y):
#             ans += arr[ni][nj]
    
#     print(ans)

prefix_sum = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        prefix_sum[i][j] = arr[i - 1][j - 1] + prefix_sum[i][j - 1] + prefix_sum[i - 1][j] - prefix_sum[i - 1][j - 1]

for _ in range(K):
    i, j, x, y = map(int, input().split())
    ans = prefix_sum[x][y] - prefix_sum[x][j - 1] - prefix_sum[i - 1][y] + prefix_sum[i - 1][j - 1]
    print(ans)