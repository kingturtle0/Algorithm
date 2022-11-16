# 문자열안에 문자열
def solution(str1, str2):
    return 1 if str2 in str1 else 2

# 제곱수 판별하기
# def solution(n):
#     return 1 if n%(n**0.5)==0 else 2

def solution(n):
    return 1 if (n ** 0.5).is_integer() else 2

# 세균 증식
# def solution(n, t):
#     return n*(2**t)

def solution(n, t):
    return n << t

# 문자열 정렬하기 (2)
def solution(my_string):
    return ''.join(sorted(my_string.lower()))
