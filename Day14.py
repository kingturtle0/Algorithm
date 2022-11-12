# 가까운 수
# def solution(array, n):
#     answer = [abs(i-n) for i in sorted(array)]
#     return sorted(array)[answer.index(min(answer))]

solution=lambda a,n:sorted(a,key=lambda x:(abs(x-n),x))[0]

# 369게임
# def solution(order):
#     return len([i for i in str(order) if i in '369'])

def solution(order):
    return sum(map(lambda x: str(order).count(str(x)), '369'))

# 암호 해독
# def solution(cipher, code):
#     return ''.join([i for i in cipher[code-1::code]])

def solution(cipher, code):
    return cipher[code-1::code]

# 대문자와 소문자
def solution(my_string):
    return my_string.swapcase()
