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
