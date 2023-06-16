for _ in range(int(input())):
    arr = [[1, 0], [0, 1]]
    N = int(input())
    if N > 1:
        for i in range(2, N + 1):
            zero = arr[i - 1][0] + arr[i - 2][0]
            one = arr[i - 1][1] + arr[i - 2][1]
            arr.append([zero, one])
    print(*arr[N])