# def solution(n):
#     ans = 0
#     while n:
#         d, r = divmod(n, 2)
#         n = d
#         ans += r
#     return ans

def solution(n):
    return bin(n).count('1')