for _ in range(int(input())):
    N = input()
    num = str(int(N) + int(N[::-1]))
    if num == num[::-1]:
        print('YES')
    else:
        print('NO')
