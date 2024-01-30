# def solution(N, stages):
#     answer = []
#     n = len(stages)
#     player = [0] * (N + 2)
#     for i in range(1, N + 2):
#         player[i] = stages.count(i)
        
#     for i in range(1, N + 1):
#         d = player[i]
#         r = n - player[i - 1]
#         n -= player[i - 1]
#         answer.append((i, d / r if r else 0))
#     answer.sort(key=lambda x:x[1], reverse=True)
#     return [idx for idx, _ in answer]

def solution(N, stages):
    answer = []
    total = len(stages)
    prev = 0
    for i in range(1, N + 1):
        yet = stages.count(i)
        cur = total - prev
        total -= prev
        prev = yet
        answer.append((i, yet / cur if cur else 0))

    answer.sort(key=lambda x:x[1], reverse=True)
    return [idx for idx, _ in answer]