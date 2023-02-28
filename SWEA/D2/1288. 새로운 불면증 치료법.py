T = int(input())

for test_case in range(1, T + 1):
    num = int(input())

    sheep = num
    num_list = []
    while set(num_list) != {0,1,2,3,4,5,6,7,8,9}:
        for i in str(sheep):
            num_list.append(int(i))
        sheep += num
        
    print(f'#{test_case} {sheep - num}')

# 다시 푼 코드
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    i = 0
    lst = []
    while True:
        i += 1
        ans = N*i
        for s in str(ans):
            lst.append(int(s))

        if set(lst) == {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}:
            break

    print(f'#{test_case}', ans)