def solution(absolutes, signs):
    length = len(signs)
    answer = 0
    for i in range(length):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer