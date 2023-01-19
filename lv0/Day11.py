# 주사위의 개수
def solution(box, n):
    answer = 1
    for i in box:
        answer *= i//n
    return answer

# def solution(box, n):
#     w,h,d = box[0]//n,box[1]//n,box[2]//n 
#     return w*d*h

# 합성수 찾기
# def solution(n):
#     answer = 0
#     if n<=10:
#         for i in range(1,n+1):
#             if i not in [1,2,3,5,7]:
#                 answer += 1
#         return answer
#     else:
#         for i in range(10,n+1):
#             if i%10 not in [1,3,7,9] or i%2==0 or i%3==0 or i%5==0 or i%7==0:
#                 answer += 1
#         return answer+4

def is_composite_num(num):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False

def solution(n):
    return len([x for x in range(1, n + 1) if is_composite_num(x)])

# 최댓값 만들기(1)
def solution(numbers):
    return sorted(numbers)[-1]*sorted(numbers)[-2]

# 팩토리얼
# def factorial(num):
#     result = 1
#     for i in range(1, num + 1):
#         result *= i
#     return result

def factorial(num): #재귀함수 팩토리얼
    if n == 0:
        return 1
    return n * factorial(num)

# def solution(n):
#     answer = 0
#     while n>=factorial(answer):
#         answer += 1
#     return answer-1

#from math import factorial

# def solution(n):
#    k = 10
#    while n < factorial(k):
#        k -= 1
#    return k
