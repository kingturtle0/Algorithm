def solution(left, right):
    answer = 0
    for number in range(left, right + 1):
        sqrt = number ** 0.5
        if sqrt - int(sqrt) > 0:
            answer += number
        else:
            answer -= number
    return answer