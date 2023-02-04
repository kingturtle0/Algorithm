T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    carrots = list(map(int, input().split()))

    counts = [0] * N
    for i in range(N - 1):
        if carrots[i + 1] > carrots[i]:
            counts[i] = 1

    for i in range(N-1):
        if counts[i+1]:
            counts[i+1] += counts[i]

    max_cnt = counts[0]
    for i in range(1, N):
        if counts[i] > max_cnt:
            max_cnt = counts[i]

    print(f'#{test_case} {max_cnt+1}')


# 더 간단하게 해결
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    carrots = list(map(int, input().split()))

    max_cnt = cnt = 1
    for i in range(N-1):
        if carrots[i+1] > carrots[i]:
            cnt += 1
            if max_cnt < cnt:
                max_cnt = cnt
        else:
            cnt = 1

    print(f'#{test_case}', max_cnt)