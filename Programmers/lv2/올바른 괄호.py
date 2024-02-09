# def solution(s):
#     stack = []
#     for i in s:
#         if i == "(":
#             stack.append(i)
#         else:
#             if stack and stack[-1] == "(":
#                 stack.pop()
#             else:
#                 return False
#     if stack:
#         return False
#     return True

def solution(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            try:
                stack.pop()
            except IndexError:
                return False
    if stack:
        return False
    return True