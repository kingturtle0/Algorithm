# 배열 자르기
def solution(numbers, num1, num2):
    return numbers[num1:num2+1]
  
# 외계행성의 나이
# def solution(age):
#     answer = ''
#     for i in str(age):
#         answer += chr(int(i)+ord('a'))
#     return answer

# def solution(age):
#     str_age = str(age)
#     answer = ''
#     lst =["a","b","c","d","e","f","g","h","i","j"]
#     for ch in str_age:
#         for i in range(0,10):
#             if int(ch) == i:
#                 answer += lst[i]
#     return answer

def solution(age):
    return ''.join([chr(ord('a')+int(i)) for i in str(age)])

# 진료순서 정하기
# def solution(emergency):
#     answer = list(range(len(emergency)))
#     rank = 1
#     while sum(emergency) != 0:
#         answer[emergency.index(max(emergency))] = rank
#         emergency[emergency.index(max(emergency))] = 0
#         rank += 1
#     return answer

def solution(emergency):
    return [sorted(emergency, reverse=True).index(i)+1 for i in emergency]
  
# 순서쌍의 개수
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i==0:
            answer+=1
    return answer
