def solution(arr):
    answer = [arr[0]]
    for number in arr:
        if number != answer[-1]:
            answer.append(number)
    return answer

def solution(arr):
    answer = [arr[0]]
    temp = answer[-1]
    for number in arr:
        if number != temp:
            answer.append(number)
            temp = number
    return answer