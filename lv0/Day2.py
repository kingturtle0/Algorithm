# 

# 숫자 비교하기
# def solution(num1, num2):
#     if num1==num2:
#         answer = 1
#     else:
#         answer = -1
#     return answer

def solution(num1, num2):
    return 1 if num1==num2 else -1
  
# 분수의 덧셈
#   def greatest_common_divisor(x, y):
#     while x%y!=0:
#         r=x%y
#         x=y
#         y=r
#     return y
    
# def solution(denum1, num1, denum2, num2):
#     a=denum1*num2+denum2*num1
#     b=num1*num2
#     gcd=greatest_common_divisor(a, b)
#     answer = [a/gcd, b/gcd]
#     return answer

import math

def solution(denum1, num1, denum2, num2):
    denum = denum1 * num2 + denum2 * num1
    num = num1 * num2
    gcd = math.gcd(denum, num)
    return [denum//gcd, num//gcd]
  
# 배열 두 배 만들기
# def solution(numbers):
#     answer = []
#     for number in numbers:
#         answer.append(number*2)
#     return answer

def solution(numbers):
    return [num*2 for num in numbers]
