# 모음 제거
# def solution(my_string):
#     for i in ['a', 'e', 'i', 'o', 'u']:
#         my_string = my_string.replace(i, '')
#     return my_string

def solution(my_string):
    return "".join([i for i in my_string if not(i in "aeiou")])

# 문자열 정렬하기 (1)
# def solution(my_string):
#     answer = []
#     for string in my_string:
#         if string.isnumeric():
#             answer += [int(string)]
#     return sorted(answer)

def solution(my_string):
    return sorted([int(string) for string in my_string if string.isnumeric()])

# 숨어있는 숫자의 덧셈 (1)
def solution(my_string):
    return sum([int(string) for string in my_string if string.isnumeric()])

# 소인수분해
# def isprime(n):
#         for i in range(2, int(n**(1/2))+1):
#             if n%i==0:
#                 return False
#         return True

# def solution(n):
#     answer = [i for i in range(2, n+1) if n%i==0]
#     return [j for j in answer if isprime(j)]

def solution(n):
    answer = []
    d = 2
    while d <= n:
        if n % d == 0:
            n /= d
            if d not in answer:
                answer.append(d)
        else:
            d += 1
    return answer
