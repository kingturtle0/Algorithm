def lenPalin(lst):
    for i in range(100, 0, -1):
        for j in range(101-i):
            ret = lst[j:j+i]
            if ret == ret[::-1]:
                return len(ret)


for test_case in range(10):
    n = int(input())
    arr = [list(input()) for _ in range(100)]

    tarr = [['' for _ in range(100)] for _ in range(100)]
    for i in range(100):
        for j in range(100):
            if i != j:
                tarr[i][j] = arr[j][i]
            else:
                tarr[i][j] = arr[i][j]

    max_val = 0
    for i in range(100):
        ret = lenPalin(arr[i])
        if max_val < ret:
            max_val = ret

        tret = lenPalin(tarr[i])
        if max_val < tret:
            max_val = tret

    print(f'#{n}', max_val)
