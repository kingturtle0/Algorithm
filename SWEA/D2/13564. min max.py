T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    max_num = numbers[0]
    min_num = numbers[0]
    for i in range(1, N):
        if numbers[i] > max_num:
            max_num = numbers[i]
        elif numbers[i] < min_num:
            min_num = numbers[i]

    result = max_num - min_num
    print(f'#{test_case} {result}')