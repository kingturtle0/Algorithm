def solution(s, n):
    answer = ''
    for alpha in s:
        if alpha.isalpha():
            cur = ord(alpha)
            new = cur + n
            if ord('A') <= cur <= ord('Z'):
                if new > ord('Z'):
                    answer += chr(new - 26)
                else:
                    answer += chr(new)
            else:
                if new > ord('z'):
                    answer += chr(new - 26)
                else:
                    answer += chr(new)
        else:
            answer += alpha
    return answer