T = int(input())

for test_case in range(1, T + 1):
    arr = [0] + list(map(int, input()))

    i = 1
    total = ans = 0
    while i < len(arr):
        if total >= (i-1):
            total += arr[i]
            i += 1
        else:
            total += 1
            ans += 1

    print(f'#{test_case}', ans)