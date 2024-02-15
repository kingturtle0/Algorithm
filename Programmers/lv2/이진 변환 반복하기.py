def solution(s):
    cnt, total = 0, 0
    while s != "1":
        cnt += 1
        total += s.count('0')
        s = s.replace('0', '')
        s = bin(len(s))[2:]
    return [cnt, total]