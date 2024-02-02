# def solution(dartResult):
#     answer = []
#     zone = {"S": 1, "D": 2, "T": 3}
#     dartResult = dartResult.replace("10", "A")
#     for result in dartResult:
#         if result.isdigit() or result == "A":
#             answer.append(10 if result == "A" else int(result))
#         elif result in zone:
#             answer[-1] **= zone[result]
#         elif result == "*":
#             cur = answer.pop()
#             if answer:
#                 answer[-1] *= 2
#             answer.append(cur * 2)
#         elif result == "#":
#             answer[-1] *= -1
#     return sum(answer)

import re

def solution(dartResult):
    answer = []
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    games = p.findall(dartResult)
    for i in range(3):
        if games[i][2] == '*' and answer:
            answer[i - 1] *= 2
        answer.append(int(games[i][0]) ** bonus[games[i][1]] * option[games[i][2]])
    return sum(answer)