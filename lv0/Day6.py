#문자열 뒤집기
# def solution(my_string):
#     answer = ''
#     for i in range(len(my_string)):
#         answer += my_string[-(i+1)]
#     return answer

def solution(my_string):
    return my_string[::-1]

#직각삼각형 출력하기
n = int(input())
for i in range(n):
    print("*"*(i+1))

#짝수 홀수 개수
# def solution(num_list):
#     answer = []
#     for num in num_list:
#         answer.append(num%2)
#     return [answer.count(0), answer.count(1)]

# def solution(num_list):
#     div_num_list = list(map(lambda v: v % 2, num_list))
#     return [div_num_list.count(0), div_num_list.count(1)]

def solution(num_list):
    answer = [0,0]
    for n in num_list:
        answer[n%2]+=1
    return answer

#문자 반복 출력하기
# def solution(my_string, n):
#     answer = ''
#     for string in my_string:
#         answer += string*n
#     return answer

def solution(my_string, n):
    return ''.join(string*n for string in my_string)
