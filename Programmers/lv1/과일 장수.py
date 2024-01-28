# def solution(k, m, score):
#     answer = 0
#     score.sort(reverse=True)
#     for i in range(0, len(score), m):
#         box = score[i:i+m]
#         n = len(box)
#         if n < m:
#             break
#         answer += min(box)*len(box)
#     return answer

def solution(k, m, score):
    return sum(sorted(score)[len(score)%m::m])*m