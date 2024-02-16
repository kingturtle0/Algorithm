def solution(n):
    answer = n + 1
    cnt = bin(n).count('1')
    while cnt != bin(answer).count('1'):
        answer += 1
    return answer