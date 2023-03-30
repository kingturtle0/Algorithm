T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    lst = []
    for _ in range(N):
        lst.append(list(map(int, input().split())))

    lst.sort(key=lambda x:x[1])

    ans = 1
    prev = lst[0][1]
    for i in range(1, N):
        if lst[i][0] >= prev:
            prev = lst[i][1]
            ans += 1

    print(f'#{test_case}', ans)