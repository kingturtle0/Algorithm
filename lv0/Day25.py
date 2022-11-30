# 문자열 밀기
# def solution(A, B):
#     answer = 0
#     while A!=B:
#         A = A[-1]+A[:-1]
#         answer += 1
#         if answer>=len(A):
#             return -1
#     return answer

solution=lambda a,b:(b*2).find(a)

# 종이 자르기
def solution(M, N):
    return M*N-1

# 연속된 수의 합
# def solution(num, total):
#     if num%2==0:
#         answer = list(range(int(total/num)-int(num/2)+1,int(total/num)+int(num/2)+1))
#     else:
#         answer = list(range(int(total/num)-int(num/2),int(total/num)+int(num/2)+1))
#     return answer

def solution(num, total):
    answer = []
    var = sum(range(num+1))
    diff = total - var
    start_num = diff//num
    answer = [i+1+start_num for i in range(num)]
    return answer

# 다음에 올 숫자
def solution(common):
    answer = 0
    if common[1]-common[0]==common[2]-common[1]:
        answer = common[-1]+common[1]-common[0]
    else:
        answer = common[-1]*(common[1]/common[0])
    return answer
