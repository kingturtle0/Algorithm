# 7의 개수
# def solution(array):
#     return ''.join([str(i) for i in array]).count("7")

def solution(array):
    return str(array).count('7')

# 잘라서 배열로 저장하기
# def solution(my_str, n):
#     answer = []
#     for i in range(0,len(my_str),n):
#         answer.append(my_str[i:i+n])
#     return answer

def solution(my_str, n):
    return [my_str[i: i + n] for i in range(0, len(my_str), n)]

# 중복된 숫자 개수
def solution(array, n):
    return array.count(n)

# 머쓱이보다 키 큰 사람
def solution(array, height):
    return len([i for i in array if i > height])
