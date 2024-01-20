def solution(arr, divisor):
    answer = sorted([element for element in arr if element % divisor == 0])
    return answer if answer else [-1]
