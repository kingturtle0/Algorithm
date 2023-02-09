T = int(input())

for test_case in range(1, T + 1):
    symbol, N = input().split()

    N = int(N)
    numbers = list(input().split())

    numdic = {"ZRO":0, "ONE":1, "TWO":2,
              "THR":3, "FOR":4, "FIV":5,
              "SIX":6, "SVN":7, "EGT":8, "NIN":9}

    bucket = [0]*10
    for i in range(N):
        bucket[numdic[numbers[i]]] += 1

    for i in range(9):
        bucket[i+1] += bucket[i]

    result = [0]*N
    for i in range(N):
        val = numdic[numbers[i]]
        result[bucket[val]-1] = numbers[i]
        bucket[val] -= 1

    print(symbol)
    for number in result:
        print(number, end=' ')