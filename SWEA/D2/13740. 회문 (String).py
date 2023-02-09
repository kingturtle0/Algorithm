T = int(input())

def findPalin(y, x):
    mystr1 = mystr2 = ''
    for i in range(M):
        for j in range(M):
            mystr1 += arr[i+y][j+x]
        if mystr1 == mystr1[::-1]:
            return mystr1
        else:
            mystr1 = ''

    for j in range(M):
        for i in range(M):
            mystr2 += arr[i+y][j+x]
        if mystr2 == mystr2[::-1]:
            return mystr2
        else:
            mystr2 = ''

    return 0

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    for i in range(N-M+1):
        for j in range(N-M+1):
            result = findPalin(i, j)
            if result:
                break

    print(f'#{test_case}', result)