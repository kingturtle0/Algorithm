# 특정 문자 제거하기
def solution(my_string, letter):
    return my_string.replace(letter, '')

# 각도기
# def solution(angle):
#     answer = 0
#     if angle < 90:
#         answer=1
#     elif angle == 90:
#         answer=2
#     elif angle < 180:
#         answer=3
#     elif angle == 180:
#         answer=4
#     return answer

def solution(angle):
    return (angle // 90) * 2 + (angle % 90 > 0) * 1

# 양꼬치
def solution(n, k):
    return n*12000 + (k-n//10)*2000

# 짝수의 합
# def solution(n):
#     return n//2 * (2 + (n if n%2==0 else n-1)) / 2

def solution(n):
    return sum([i for i in range(2, n + 1, 2)])
