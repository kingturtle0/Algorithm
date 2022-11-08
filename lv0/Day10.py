# 점의 위치 구하기
# def solution(dot):
#     if dot[0]>0 and dot[1]>0:
#         return 1
#     elif dot[0]<0 and dot[1]>0:
#         return 2
#     elif dot[0]<0 and dot[1]<0:
#         return 3
#     else:
#         return 4

def solution(dot):
    quad = [(3,2),(4,1)]
    return quad[dot[0] > 0][dot[1] > 0]

# 2차원으로 만들기
def solution(num_list, n):
    return [num_list[i:i+n] for i in range(0,len(num_list),n)]

# import numpy as np
# def solution(num_list, n):
#     li = np.array(num_list).reshape(-1,n)
#     return li.tolist()

# 공 던지기
# def solution(numbers, k):
#     answer = 0
#     n = 0
#     while k!=0:
#         answer = numbers[n]
#         n += 2
#         if n >= len(numbers):
#             n = n-len(numbers)
#         k -= 1
#     return answer

# from collections import deque
# def solution(numbers, k):
#     array = deque(numbers)
#     array.rotate(-(k-1)*2)
#     return array[0]

def solution(numbers, k):
    return numbers[(2*k-2)%len(numbers)]

# 배열 회전시키기
# def solution(numbers, direction):
#     if direction == "right":
#         return [numbers[i-1] for i in range(len(numbers))]
#     else:
#         return [numbers[i+1-len(numbers)] for i in range(len(numbers))]

# def solution(numbers, direction):
#     return [numbers[-1]] + numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]

from collections import deque
def solution(numbers, direction):
    numbers = deque(numbers)
    numbers.rotate(1 if direction == 'right' else -1)
    return list(numbers)
