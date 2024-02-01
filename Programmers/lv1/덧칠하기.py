def solution(n, m, section):
    answer = 0
    start = 0
    for num in section:
        if num > start:
            answer += 1
            start = num + m - 1
    return answer