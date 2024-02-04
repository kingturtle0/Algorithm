# def solution(X, Y):
#     inter = sorted(set(X) & set(Y), reverse=True)
#     if len(inter) == 1 and inter[0] == '0':
#         return '0'
    
#     if inter:
#         return ''.join([num * min(X.count(num), Y.count(num)) for num in inter])
#     else:
#         return '-1'

def solution(X, Y):
    answer = ''
    for i in range(9,-1,-1):
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))

    if answer == '':
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else:
        return answer