import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[0]*(N+1)]
darr = [[0]*(N+1) for _ in range(N+1)]

for i in range(N):
    arow = [0] + list(map(int, input().split()))
    arr.append(arow)

for i in range(1, N+1):
    for j in range(1, N+1):
        darr[i][j] = darr[i][j-1] + darr[i-1][j] -darr[i-1][j-1] + arr[i][j]

for tc in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    result = darr[x2][y2] - darr[x1-1][y2] - darr[x2][y1-1] + darr[x1-1][y1-1]
    print(result)