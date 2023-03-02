T = int(input())

for test_case in range(1, T + 1):
    lst = list(map(int, input().split()))
    tc, lst = lst[0], lst[1:]

    ans = 0
    for i in range(19):
        for j in range(i+1, 20):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
                ans += 1

    print(tc, ans)