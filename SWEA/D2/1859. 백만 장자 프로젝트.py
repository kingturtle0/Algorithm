T = int(input())

for test_case in range(1, T + 1):
    count = int(input())
    price_list = list(map(int, input().split()))

    profit = 0
    for i in range(count):
        for j in range(i + 1, count):
            if price_list[i] < price_list[j]:
                profit += (max(price_list[j:]) - price_list[i])
                break

    print(f"#{test_case} {profit}")
    
# 런타임 에러(2중 for문)

T = int(input())

for test_case in range(1, T + 1):
    length = int(input())
    prices = list(map(int, input().split()))

    cnt = 0
    profit = 0
    for i in range(length-1, 0, -1):
        if prices[i+cnt] > prices[i-1]:
            profit += (prices[i+cnt] - prices[i-1])
            cnt += 1
        else:
            cnt = 0

    print(f'#{test_case} {profit}')
    
# 1중 for문으로 해결
