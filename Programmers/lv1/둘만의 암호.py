# def solution(s, skip, index):
#     answer = ''
#     rules = []
#     for i in range(26):
#         temp = chr(i + ord('a'))
#         if temp not in skip:
#             rules.append(temp)
#     rules = rules * 3
#     for i in s:
#         answer += rules[rules.index(i) + index]
#     return answer

def solution(s, skip, index):
    alphas = [chr(a) for a in range(ord("a"), ord("z")+1) if chr(a) not in skip]
    return "".join([alphas[(alphas.index(a) + index) % len(alphas)] for a in s])