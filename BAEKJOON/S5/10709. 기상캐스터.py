H, W = map(int, input().split())
arr = [list(input()) for _ in range(H)]

for i in range(H):
    for j in range(W):
        if arr[i][j] == 'c':
            cnt = 1
            arr[i][j] = 0
            for k in range(j+1, W):
                if arr[i][k] == '.':
                    arr[i][k] = cnt
                    cnt += 1
                else:
                    arr[i][k] = 0
                    cnt = 1
        elif arr[i][j] == '.':
            arr[i][j] = -1

for lst in arr:
    print(*lst)