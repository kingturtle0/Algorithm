def solution(s):
    length = len(s)
    return s.isnumeric() and (length == 4 or length == 6)