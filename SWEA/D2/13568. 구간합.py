T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    sums = [0] * (N-M+1)
    for i in range(N-M+1):
        for j in range(i, i+M):
            sums[i] += numbers[j]

    max_val = sums[0]
    min_val = sums[0]
    for i in range(1, N-M+1):
        if sums[i] > max_val:
            max_val = sums[i]
        elif sums[i] < min_val:
            min_val = sums[i]

    result = max_val - min_val
    print(f'#{test_case} {result}')
    