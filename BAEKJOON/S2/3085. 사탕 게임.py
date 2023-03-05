N = int(input())
arr = [list(input()) for _ in range(N)]


def maxcandy(arr):
    ret = 1
    for i in range(N):
        cnt = 1
        for j in range(N - 1):
            if arr[i][j] == arr[i][j + 1]:
                cnt += 1
                ret = max(ret, cnt)
            else:
                cnt = 1

    for i in range(N):
        cnt = 1
        for j in range(N - 1):
            if arr[j][i] == arr[j + 1][i]:
                cnt += 1
                ret = max(ret, cnt)
            else:
                cnt = 1

    return ret


ans = maxcandy(arr)
for ci in range(N):
    for cj in range(N):
        cnt = 0
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj

            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != arr[ci][cj]:
                arr[ci][cj], arr[ni][nj] = arr[ni][nj], arr[ci][cj]
                cnt = maxcandy(arr)
                arr[ci][cj], arr[ni][nj] = arr[ni][nj], arr[ci][cj]
                ans = max(ans, cnt)

print(ans)