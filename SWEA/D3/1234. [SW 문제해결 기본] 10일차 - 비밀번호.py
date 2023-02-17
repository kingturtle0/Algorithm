for test_case in range(1, 11):
    n, st = input().split()

    lst = []
    for i in range(int(n)):
        if not lst:
            lst.append(st[i])
        else:
            if lst[-1] == st[i]:
                lst.pop()
            else:
                lst.append(st[i])


    print(f'#{test_case}', ''.join(lst))