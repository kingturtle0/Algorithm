# 컨트롤 제트
def solution(s):
    answer = []
    for i in s.split(' '):
        if i.isalpha():
            answer = answer[:-1]
        else:
            answer.append(int(i))
    return sum(answer)

# 배열 원소의 길이
def solution(strlist):
    return [len(i) for i in strlist]

# 중복된 문자 제거
def solution(my_string):
    answer = ''
    for string in my_string:
        if string not in answer:
            answer += string
    return answer

# def solution(my_string):
#     return ''.join(dict.fromkeys(my_string))

# 삼각형의 완성조건 (1)
# def solution(sides):
#     sides.sort()
#     return 1 if sides[0]+sides[1]>sides[2] else 2
    
def solution(sides):
    return 1 if max(sides) < (sum(sides) - max(sides)) else 2
