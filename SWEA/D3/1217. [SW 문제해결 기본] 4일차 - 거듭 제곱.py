for test_case in range(10):
    tc = int(input())
    N, M = map(int, input().split())
    ans = 1

    def power(level):
        global ans, N, M

        if level == M:
            return

        ans *= N
        power(level+1)

    power(0)
    print(f'#{tc}', ans)