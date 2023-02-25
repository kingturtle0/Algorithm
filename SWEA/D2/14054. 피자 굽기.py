T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    idx = 1
    q = [[lst[0], idx]]
    lst.pop(0)

    while q:
        if len(q) < N and lst:
            idx += 1
            item = lst.pop(0)
            q.append([item, idx])
        else:
            c = q.pop(0)
            c[0] //= 2
            if c[0] == 0:
                if lst:
                    idx += 1
                    item = lst.pop(0)
                    q.append([item, idx])
            else:
                q.append(c)

        if len(q) == 1:
            break

    print(f'#{test_case}', q[0][1])