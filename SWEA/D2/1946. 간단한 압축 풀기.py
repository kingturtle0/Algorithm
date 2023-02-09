T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    mystr = ''
    sumnum = 0
    for i in range(N):
        alpha, num = input().split()
        mystr += alpha*int(num)
        sumnum += int(num)

    print(f'#{test_case}')
    i = j = 0
    while True:
        print(mystr[i], end='')
        i += 1

        if i%10 == 0:
            print()

        if i == sumnum:
            break

    print()