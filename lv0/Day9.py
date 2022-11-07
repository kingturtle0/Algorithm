# 개미 군단
# def solution(hp):
#     answer = 0
#     if hp%5==0:
#         return hp//5
#     else:
#         answer = hp//5 + (hp%5)//3
#         if hp%5%3!=0:
#             answer += (hp%5%3)//1
#     return answer

def solution(hp):    
    return hp // 5 + (hp % 5 // 3) + ((hp % 5) % 3)

# 모스부호 (1)
morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }

# def solution(letter):
#     answer = ''
#     for m in letter.split(' '):
#         answer += morse[m]
#     return answer

def solution(letter):
    return ''.join([morse[i] for i in letter.split(' ')])

# 가위 바위 보
d = {"2":"0", "0":"5", "5":"2"}

def solution(rsp):
    return ''.join([d[i] for i in rsp])

# 구슬을 나누는 경우의 수
# def factorial(num):
#     result = 1
#     while num > 0:
#         result = result * num
#         num -= 1
#     return result

def solution(balls, share):
    return factorial(balls)/(factorial(balls-share)*factorial(share))

def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result = result * i
    return result

# import math
# def solution(balls, share):
#     return math.comb(balls, share)
