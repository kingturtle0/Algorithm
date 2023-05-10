T = int(input())

for test_case in range(T):
    N = int(input())
    arr = [1] * 12
    arr[2], arr[3] = 2, 4

    for i in range(4, 12):
        arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3]

    print(arr[N])