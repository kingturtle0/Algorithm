# def solution(nums):
#     answer = 0
#     primes = [0, 0] + [1] * 2999
#     for i in range(4, 3001):
#         for j in range(2, int(i ** 0.5) + 1):
#             if i % j == 0:
#                 primes[i] = 0
    
#     n = len(nums)
#     for i in range(n - 2):
#         for j in range(i + 1, n - 1):
#             for k in range(j + 1, n):
#                 if primes[nums[i] + nums[j] + nums[k]]:
#                     answer += 1
    
#     return answer

def solution(nums):
    answer = 0
    primes = [0] * 2 + [1] * 2999
    for i in range(2, 3001):
        if primes[i]:
            for j in range(i*2, 3001, i):
                primes[j] = 0
    
    n = len(nums)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if primes[nums[i] + nums[j] + nums[k]]:
                    answer += 1
    
    return answer