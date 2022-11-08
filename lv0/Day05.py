# 옷가게 할인 받기
# def solution(price):
#     if price >= 500000:
#         answer = price*0.8
#     elif price >= 300000:
#         answer = price*0.9
#     elif price >= 100000:
#         answer = price*0.95
#     else:
#         answer = price
#     return int(answer)

def solution(price):
    discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(price * discount_rate)
            
#아이스 아메리카노
# def solution(money):
#     return [money//5500, money%5500]

def solution(money):
    return divmod(money, 5500)
    
# 나이 출력
def solution(age):
    return 2023-age
  
# 배열 뒤집기
# def solution(num_list):
#     answer = []
#     for i in range(len(num_list)):
#         answer.append(num_list[-(i+1)])
#     return answer

# def solution(num_list):
#     num_list.reverse()
#     return num_list

def solution(num_list):
    return num_list[::-1]
