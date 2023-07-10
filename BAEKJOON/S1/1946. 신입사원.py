import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    lst = [0] * (N + 1)
    for _ in range(N):
        a, b = map(int, input().split())
        lst[a] = b

    ans = 1
    b = lst[1]
    for i in range(2, N + 1):
        if b > lst[i]:
            ans += 1
            b = lst[i]

    print(ans)