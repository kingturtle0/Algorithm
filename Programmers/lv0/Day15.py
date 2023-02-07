#영어가 싫어요
# def solution(numbers):
#     eng = {"zero":0, "one":1, "two":2, "three":3, "four":4,
#            "five":5, "six":6, "seven":7, "eight":8, "nine":9}
#     for i in list(eng):
#         if i in numbers:
#             numbers.replace(i, str(eng[i]))
#     return int(numbers)

def solution(numbers):
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(num))
    return int(numbers)

#인덱스 바꾸기
# def solution(my_string, num1, num2):
#     answer = [i for i in my_string]
#     answer[num1], answer[num2]= answer[num2], answer[num1]
#     return ''.join([i for i in answer])

def solution(my_string, num1, num2):
    s = list(my_string)
    s[num1],s[num2] = s[num2],s[num1]
    return ''.join(s)

#한 번만 등장한 문자
# def solution(s):
#     alp = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
#            "n","o","p","q","r","s","t","u","v","w","x","y","z"]
#     return ''.join([i for i in alp if s.count(i)==1])

# def solution(s):
#     return ''.join([i for i in "abcdefghijklmnopqrstuvwxyz" if s.count(i)==1])

def solution(s):
    return ''.join(sorted([i for i in s if s.count(i) == 1]))

#약수 구하기
def solution(n):
    return [i for i in range(1,n+1) if n%i==0]
