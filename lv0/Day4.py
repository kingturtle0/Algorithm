# 피자 나눠 먹기(1)
# def solution(n):
#     # if n%7==0:
#     #     answer = n/7
#     # else:
#     #     answer = n//7 + 1
#     answer = n//7.001 + 1
#     return answer

def solution(n):
    return (n - 1) // 7 + 1
  
# 피자 나눠 먹기(2)
# def solution(n):
#     piece = 6
#     while piece%n!=0:
#         piece += 6
#     answer = piece/6
#     return answer

def solution(n):
    pizza=1
    while(True):
        if (6*pizza)%n==0:
            return pizza
        pizza+=1

# 피자 나눠 먹기(3)
def solution(slice, n):
    answer = (n-1)//slice + 1
    return answer

# 배열의 평균값
# def solution(numbers):
#     return sum(numbers)/len(numbers)

import numpy as np
def solution(numbers):
    return np.mean(numbers)
