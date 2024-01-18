def solution(price, money, count):
    total = price*sum([i for i in range(1, count + 1)])
    if money - total < 0:
        return total - money
    else:
        return 0
