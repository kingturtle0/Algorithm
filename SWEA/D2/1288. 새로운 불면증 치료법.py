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
