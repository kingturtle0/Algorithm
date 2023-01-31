T = int(input())

for test_case in range(1, T + 1):
    test_str = input()[::-1]

    result = test_str.find(test_str[0], 1) - test_str.find(test_str[0])

    print(f'#{test_case} {result}')
