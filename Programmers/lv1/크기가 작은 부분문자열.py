def solution(t, p):
    answer = 0
    length_p = len(p)
    p = int(p)
    for i in range(len(t) - length_p + 1):
        if int(t[i:i+length_p]) <= p:
            answer += 1
    return answer