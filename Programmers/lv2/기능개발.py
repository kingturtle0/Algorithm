def solution(progresses, speeds):
    answer = []
    day = 1
    while progresses:
        for i in range(len(speeds)):
            progresses[i] += speeds[i]
        cnt = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        if cnt:
            answer.append(cnt)
        day += 1
    return answer