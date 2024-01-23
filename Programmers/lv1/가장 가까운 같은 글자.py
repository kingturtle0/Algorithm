# def solution(s):
#     n = len(s)
#     answer = [-1]*n
    
#     for i in range(n):
#         temp = s[i]
#         for j in range(i - 1, -1, -1):
#             if temp == s[j]:
#                 answer[i] = i - j
#                 break
#     return answer

# def solution(s):
#     n = len(s)
#     answer = [-1]*n
#     start, end = 0, 1
#     while end < n:
#         if s[start] == s[end]:
#             answer[end] = end - start
#             end += 1
#             start = end - 1
#         else:
#             start -= 1
        
#         if start == -1:
#             end += 1
#             start = end - 1
#     return answer

def solution(s):
    answer = []
    dic = dict()
    for i in range(len(s)):
        answer.append(i - dic[s[i]] if s[i] in dic else -1)
        dic[s[i]] = i
    return answer