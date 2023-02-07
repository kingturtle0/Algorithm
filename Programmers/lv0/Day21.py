# 숨어있는 숫자의 덧셈 (2)
# def solution(my_string):
#     for i in my_string:
#         if i.isalpha():
#             my_string = my_string.replace(i, " ")
#     return sum([int(i) for i in my_string.split(" ") if i.isdigit()])

def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())

# 안전지대
# def solution(board):
#     answer = 0
#     mine = []
#     length = len(board)
#     for i in range(length):
#         for j in range(length):
#             if board[i][j]==1:
#                 for k in range(i-1,i+2):
#                     for l in range(j-1,j+2):
#                         if not (k<0 or l<0 or k>=length or l>=length):
#                             mine += [k,l]
#     for i in range(0,len(mine),2):
#         board[mine[i]][mine[i+1]]=1
#     for i in board:
#         answer += i.count(0)
#     return answer

def solution(board):
    n = len(board)
    danger = set()
    for i, row in enumerate(board):
        for j, x in enumerate(row):
            if not x:
                continue
            danger.update((i+di, j+dj) for di in [-1,0,1] for dj in [-1, 0, 1])
    return n*n - sum(0 <= i < n and 0 <= j < n for i, j in danger)

# 삼각형의 완성조건 (2)
# def solution(sides):
#     return len(range(max(sides)-min(sides)+1,max(sides)+1)) + len(range(max(sides)+1,sum(sides)))

def solution(sides):
    return sum(sides) - max(sides) + min(sides) - 1

# 외계어 사전
# def solution(spell, dic):
#     answer = [i for i in range(len(dic)) for j in range(len(spell)) if spell[j] not in dic[i]]
#     if len(dic)!=len(set(answer)):
#         return 1
#     else:
#         return 2

def solution(spell, dic):
    spell = set(spell)
    for s in dic:
        if not spell-set(s):
            return 1
    return 2
