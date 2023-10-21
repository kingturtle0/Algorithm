for _ in range(int(input())):
    N, M = map(int, input().split())
    ans = 0
    for i in range(N, M + 1):
        ans += str(i).count('0')
    print(ans)