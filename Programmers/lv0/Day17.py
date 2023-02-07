#숫자 찾기
# def solution(num, k):
#     if str(k) in list(str(num)):
#         return list(str(num)).index(str(k)) + 1
#     else:
#         return -1
    
def solution(num, k):
    try:
        return str(num).index(str(k)) + 1
    except ValueError:
        return -1

#n의 배수 고르기
# def solution(n, numlist):
#     return [num for num in numlist if num%n==0]

def solution(n, numlist):
    return list(filter(lambda v: v%n==0, numlist))

#자릿수 더하기
# def solution(n):
#     return sum([int(i) for i in str(n)])

def solution(n):
    return sum(list(map(int,list(str(n)))))

#OX퀴즈
# def solution(quiz):
#     answer = []
#     for i in range(len(quiz)):
#         if eval(quiz[i].split(" = ")[0])==int(quiz[i].split(" = ")[1]):
#             answer += "O"
#         else:
#             answer += "X"
#     return answer

def valid(x):
    x = x.replace('=', '==')
    return eval(x)

def solution(quiz):
    return ["O" if valid(i) else "X" for i in quiz] 
