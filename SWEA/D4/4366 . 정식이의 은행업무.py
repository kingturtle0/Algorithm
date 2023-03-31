T = int(input())

for test_case in range(1, T + 1):
    bn = list(map(int, input()))
    tn = list(map(int, input()))

    binlst = []
    terlst = []
    for i in range(len(bn)):
        bn[i] = 1 - bn[i]
        bindec = int(''.join(map(str, bn)), 2)
        binlst.append(bindec)
        bn[i] = 1 - bn[i]

    for i in range(len(tn)):
        for j in range(3):
            if j != tn[i]:
                temp = tn[i]
                tn[i] = j
                terdec = int(''.join(map(str, tn)), 3)
                terlst.append(terdec)
                tn[i] = temp

    print(f'#{test_case}', *list(set(binlst) & set(terlst)))