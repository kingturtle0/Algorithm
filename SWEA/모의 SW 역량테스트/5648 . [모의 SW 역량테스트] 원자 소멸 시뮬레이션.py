T = int(input())
direct = [(1, 0), (-1, 0), (0, -1), (0, 1)]

for test_case in range(1, T + 1):
    N = int(input())
    arr = []
    for i in range(N):
        x, y, d, k = map(int, input().split())
        arr.append([y*2, x*2, d, k])

    ans = 0
    for _ in range(4000):
        for i in range(len(arr)):
            arr[i][0] += direct[arr[i][2]][0]
            arr[i][1] += direct[arr[i][2]][1]

        v = set()
        dset = set()
        for i in range(len(arr)):
            y, x = arr[i][0], arr[i][1]
            if (y, x) in v:
                dset.add((y, x))
            else:
                v.add((y, x))

        for i in range(len(arr) - 1, -1, -1):
            if (arr[i][0], arr[i][1]) in dset:
                ans += arr[i][3]
                arr.pop(i)
            elif arr[i][0] > 2000 or arr[i][0] < -2000 or arr[i][1] > 2000 or arr[i][1] < -2000:
                arr.pop(i)

    print(f'#{test_case} {ans}')