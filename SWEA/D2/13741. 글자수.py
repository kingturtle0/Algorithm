T = int(input())

for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()

    numdic = dict()
    for s2 in str2:
        if s2 in numdic:
            numdic[s2] += 1
        else:
            numdic[s2] = 0

    max_val = -(21e8)
    for s1 in str1:
        if max_val < numdic[s1]:
            max_val = numdic[s1]

    print(f'#{test_case}', max_val+1)