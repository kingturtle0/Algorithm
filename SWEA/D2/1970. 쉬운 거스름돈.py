T = int(input())

for test_case in range(1, T + 1):
    money = int(input())
    money_dic = {'50000':0, '10000':0, '5000':0, '1000':0, '500':0, '100':0, '50':0, '10':0}

    for key in money_dic:
        if money >= int(key):
            money_dic[key] += (money // int(key))
            money = (money % int(key))
    
    print(f'#{test_case}')
    for value in money_dic.values():
        print(value, end = ' ')
    print()
