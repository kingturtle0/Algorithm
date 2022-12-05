# 저주의 숫자 3
# def solution(n):
#     answer = [i for i in range(1,200) if i%3!=0 and "3" not in str(i)]
#     return answer[n-1]

def solution(n):
    answer = 0
    for _ in range(n):
        answer += 1
        while answer % 3 == 0 or '3' in str(answer):
            answer += 1
    return answer

# 평행
# def solution(dots):
#     answer = [(dots[i][1]-dots[j][1])/(dots[i][0]-dots[j][0]) for i in range(len(dots)) for j in range(i+1,len(dots))]
#     if len(answer)==len(set(answer)):
#         return 0
#     else:
#         return 1

from itertools import combinations

def solution(dots):
    a = []
    for (x1,y1),(x2,y2) in combinations(dots,2):
        a.append((y2-y1,x2-x1))

    for (x1,y1),(x2,y2) in combinations(a,2):
        if x1*y2==x2*y1:
            return 1
    return 0

# 겹치는 선분의 길이
# def solution(lines):
#     answer = [[] for _ in range(200)]
#     for idx, line in enumerate(lines):
#         x, y = line
#         for i in range(x, y):
#             answer[i+100].append(idx)
#     return len([i for i in answer if len(i)>1])

def solution(lines):
    sets = [set(range(min(l), max(l))) for l in lines]
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])

# 유한소수 판별하기
# def greatest_common_divisor(x, y):
#     while x%y!=0:
#         r=x%y
#         x=y
#         y=r
#     return y

# def is_composite_num(num):
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 return False
#         return True

# def solution(a, b):
#     b = int(b/greatest_common_divisor(a, b))
#     answer = [i for i in range(1,b+1) if b%i==0 and is_composite_num(i)]
#     x = 0
#     for i in answer:
#         if i not in [1,2,5]:
#             x+=1
#     if x==0:
#         return 1
#     else:
#         return 2
        
from math import gcd
def solution(a, b):
    b //= gcd(a,b)
    while b%2==0:
        b//=2
    while b%5==0:
        b//=5
    return 1 if b==1 else 2
