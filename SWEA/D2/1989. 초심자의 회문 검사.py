T = int(input())

for test_case in range(1, T + 1):
    palindrome = input()
    if palindrome == palindrome[::-1]:
        flag = 1
    else:
        flag = 0
    print(f'#{test_case} {flag}')
