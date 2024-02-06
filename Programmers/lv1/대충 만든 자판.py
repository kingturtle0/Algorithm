def solution(keymap, targets):
    answer = []
    mins = [100] * 26
    for key in keymap:
        for i in range(26):
            temp = key.find(chr(i + ord('A'))) + 1
            if temp:
                mins[i] = min(mins[i], temp)
    for i in range(26):
        if mins[i] == 100:
            mins[i] = 0
    
    for target in targets:
        cnt = 0
        for s in target:
            temp = mins[ord(s) - ord('A')]
            if temp:
                cnt += temp
            else:
                cnt = -1
                break
        answer.append(cnt)
    return answer