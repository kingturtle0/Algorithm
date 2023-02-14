T = int(input())

def isSudoku(y, x, arr):
    lst = []
    for i in range(3):
        for j in range(3):
            lst.append(arr[y+i][x+j])
    return set(lst)

for test_case in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    tarr = [[0 for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            if i < j:
                tarr[i][j] = arr[j][i]
            elif i > j:
                tarr[i][j] = arr[j][i]
            else:
                tarr[i][j] = arr[i][j]

    flag = 1
    for i in range(9):
        if set(arr[i]) != set(range(1,10)) or set(tarr[i]) != set(range(1,10)):
            flag = 0
            break

    for i in (0, 3, 6):
        for j in (0, 3, 6):
            if isSudoku(i, j, arr) != set(range(1, 10)):
                flag = 0
                break

    print(f'#{test_case}', flag)