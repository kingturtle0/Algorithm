T = int(input())

for test_case in range(1, T + 1):
    arr = [['']*15 for _ in range(5)]

    arr2 = [list(input()) for _ in range(5)]
    for i in range(5):
        arr[i][:len(arr2[i])] = arr2[i]

    ans = ''
    for j in range(15):
        for i in range(5):
            if arr[i][j]:
                ans += arr[i][j]

    print(f'#{test_case}', ans)