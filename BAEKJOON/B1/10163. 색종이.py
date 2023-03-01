arr = [[0]*1001 for _ in range(1001)]

N = int(input())

for k in range(1, N+1):
    x, y, w, h = map(int, input().split())
    for j in range(x, x+w):
        for i in range(y, y+h):
            arr[i][j] = k

for k in range(1, N+1):
    ans = 0
    for i in range(1001):
        for j in range(1001):
            if arr[i][j] == k:
                ans += 1
    print(ans)