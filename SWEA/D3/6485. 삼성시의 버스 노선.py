T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    counts = [0]*5001

    for _ in range(N):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            counts[i] += 1

    P = int(input())
    routes = [counts[int(input())] for _ in range(P)]

    print(f'#{test_case}', end=' ')
    for route in routes:
        print(route, end=' ')
    print()
    