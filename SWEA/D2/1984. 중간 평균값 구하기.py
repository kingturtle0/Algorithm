T = int(input())

for test_case in range(1, T + 1):
    num_list = list(map(int, input().split()))
    result = sorted(num_list)
    total = 0
    for i in result[1:len(result)-1]:
        total += i

    avg = total / (len(result) - 2)

    print(f'#{test_case} {round(avg)}')
