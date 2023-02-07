# 나머지 구하기
# def solution(num1, num2):
#     answer = num1 % num2
#     return answer

def solution(num1, num2):
    return num1 % num2
  
# 중앙값 구하기
def solution(array):
    # array.sort()
    # index = int(len(array)/2)
    # answer = array[index]
    return sorted(array)[len(array) // 2]

# 최빈값 구하기
# def solution(array):
#     array.sort()
#     cnt = []
#     for num in array:
#         cnt.append(array.count(num))
#     mx = max(cnt)
#     if mx != cnt.count(mx):
#         return -1
#     ind = cnt.index(mx)
#     answer = array[ind]
#     return answer

def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0: return a
    return -1
  
# 짝수는 싫어요
# def solution(n):
#     answer = []
#     for num in range(1, n+1, 2):
#         answer.append(num)
#     return answer

def solution(n):
    return [i for i in range(1, n+1, 2)]
