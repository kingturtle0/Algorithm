T = int(input())

for test_case in range(1, T + 1):
    st = input()

    ans = 1
    flag = 0
    lst = []
    for s in st:
        if s =='(':
            lst.append(s)
        elif s == '{':
            lst.append(s)

        if s == '}':
            if lst:
                if lst.pop() != '{':
                    flag = 1
                    break
            else:
                flag = 1
                break
        elif s == ')':
            if lst:
                if lst.pop() != '(':
                    flag = 1
                    break
            else:
                flag = 1
                break

    if flag:
        ans = 0

    if lst:
        ans = 0

    print(f'#{test_case}', ans)