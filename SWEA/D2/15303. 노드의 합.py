T = int(input())

for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())
    arr = [0]*(N+2)

    for i in range(M):
        idx, val = map(int, input().split())
        if idx % 2 == 0:
            arr[idx] = val
        else:
            arr[idx] = val

    for i in range(N//2, 0, -1):
        arr[i] = arr[i*2] + arr[i*2+1]

    print(f'#{test_case}', arr[L])