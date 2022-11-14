# 편지
def solution(message):
    return len(message)*2

# 가장 큰 수 찾기
def solution(array):
    return [max(array), array.index(max(array))]

# 문자열 계산하기
# def solution(my_string):
#     my_string = my_string.replace("+ ", "").replace("- ", "-")
#     return sum([int(i) for i in my_string.split(" ")])

# def solution(my_string):
#     return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))

# def solution(my_string):
#     return eval(my_string)

solution=eval

# 배열의 유사도
# def solution(s1, s2):
#     answer = 0
#     for i in s1:
#         if i in s2:
#             answer += 1
#     return answer

def solution(s1, s2):
    return len(set(s1)&set(s2))
