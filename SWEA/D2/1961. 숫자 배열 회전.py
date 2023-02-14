T = int(input())

def rotate(arr, N):
    result = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result[j][N - 1 - i] = str(arr[i][j])

    return result

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = [['']*3 for _ in range(N)]
    for i in range(3):
        arr = rotate(arr, N)
        for j in range(N):
            result[j][i] = ''.join(arr[j])

    print(f'#{test_case}')
    for i in range(N):
        for j in range(3):
            print(result[i][j], end=' ')
        print()