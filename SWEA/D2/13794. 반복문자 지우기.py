T = int(input())

for test_case in range(1, T + 1):
    st = input()

    lst = []

    for s in st:
        if not lst:
            lst.append(s)
        else:
            if s == lst[-1]:
                lst.pop()
            else:
                lst.append(s)

    print(f'#{test_case}', len(lst))