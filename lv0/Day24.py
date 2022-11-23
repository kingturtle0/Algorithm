# 이진수 더하기
# def bintoint(x):
#     n=0
#     lng = len(x)
#     for i in x:
#         lng-=1
#         n += int(i)*pow(2, lng)
#     return n

# def solution(bin1, bin2):
#     return bin(bintoint(bin1)+bintoint(bin2))[2:]

def solution(bin1, bin2):
    return bin(int(bin1,2) + int(bin2,2))[2:]
  
# A로 B 만들기
# def solution(before, after):
#     answer = 1
#     for i in before:
#         if before.count(i)==after.count(i):
#             answer *= 1
#         else:
#             answer *=0
#     return answer

def solution(before, after):
    return 1 if sorted(before)==sorted(after) else 0

# k의 개수
def solution(i, j, k):
    return sum([str(x).count(str(k)) for x in range(i,j+1)])
  
# 
