T = int(input())

for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = []
    direct = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
    oppo = (0, 2, 1, 4, 3)
    for _ in range(K):
        arr.append(list(map(int, input().split())))

    for _ in range(M):
        for k in range(len(arr)):
            y, x, n, d = arr[k]
            ny, nx = y + direct[d][0], x + direct[d][1]
            if not n:
                continue

            if ny < 0 or nx < 0 or ny >= N or nx >= N:
                continue
            elif 0 < ny < N - 1 and 0 < nx < N - 1:
                arr[k] = [ny, nx, n, d]
            else:
                arr[k] = [ny, nx, n//2, oppo[d]]

        arr.sort(key=lambda x:(x[0], x[1], x[2]), reverse=True)

        idx = 1
        while idx < len(arr):
            if arr[idx][0] == arr[idx - 1][0] and arr[idx][1] == arr[idx - 1][1]:
                arr[idx - 1][2] += arr[idx][2]
                arr.pop(idx)
            else:
                idx += 1

    ans = 0
    for y, x, n, d in arr:
        ans += n

    print(f'#{test_case} {ans}')