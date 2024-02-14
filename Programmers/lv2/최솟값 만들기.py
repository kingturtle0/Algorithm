# def solution(A,B):
#     answer = 0
#     A.sort()
#     B.sort(reverse=True)
#     for i in range(len(A)):
#         answer += A[i] * B[i]
#     return answer

def solution(A, B):
    return sum(map(lambda a, b: a * b, sorted(A), sorted(B, reverse=True)))