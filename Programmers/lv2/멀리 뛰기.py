# def solution(n):
#     answer = [1] * (n + 1)
#     for i in range(2, n + 1):
#         answer[i] = answer[i - 1] + answer[i - 2]
#     return answer[n] % 1234567

def solution(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return b % 1234567