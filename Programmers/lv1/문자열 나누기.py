from collections import deque

def solution(s):
    answer = 0
    q = deque(s)
    x = q[0]
    cnt_x, cnt_xx = 0, 0
    while q:
        xx = q.popleft()
        if xx == x:
            cnt_x += 1
        else:
            cnt_xx += 1
        
        if cnt_x == cnt_xx:
            answer += 1
            if q:
                x = q[0]
                cnt_x, cnt_xx = 0, 0
        else:
            if not q:
                answer += 1
    return answer