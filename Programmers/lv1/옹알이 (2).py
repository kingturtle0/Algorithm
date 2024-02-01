def iscontinuous(word):
    for run in ("11", "22", "33", "44"):
        if run in word:
            return False
    return True

def solution(babbling):
    answer = 0
    dic = {"aya": "1", "ye": "2", "woo": "3", "ma": "4"}
    for i in range(len(babbling)):
        temp = babbling[i]
        for key, value in dic.items():
            temp = temp.replace(key, value)
        if temp.isdigit() and iscontinuous(temp):
            answer += 1
    return answer