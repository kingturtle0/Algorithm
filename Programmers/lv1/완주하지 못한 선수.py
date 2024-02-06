from collections import defaultdict

def solution(participant, completion):
    dic_p = defaultdict(int)
    for p in participant:
        dic_p[p] += 1
    for c in completion:
        dic_p[c] -= 1
    for key in dic_p:
        if dic_p[key] == 1:
            return key
        
# from collections import Counter

# def solution(participant, completion):
#     return list(Counter(participant) - Counter(completion))[0]