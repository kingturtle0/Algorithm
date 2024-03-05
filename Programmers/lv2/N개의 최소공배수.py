def lcm(a, b):
    n = a * b
    a, b = max(a, b), min(a, b)
    while b:
        r = a % b
        a, b = b, r
    
    return n / a
        

def solution(arr):
    answer = arr[0]
    for n in arr:
        answer = lcm(answer, n)
    return answer