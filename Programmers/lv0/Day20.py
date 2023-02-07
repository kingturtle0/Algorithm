# 직사각형 넓이 구하기
# def solution(dots):
#     a = max([i[0] for i in dots])-min([i[0] for i in dots])
#     b = max([i[1] for i in dots])-min([i[1] for i in dots])
#     return a*b

def solution(dots):
    return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1])

# 캐릭터의 좌표
# def solution(keyinput, board):
#     answer = [0,0]
#     for i in keyinput:
#         if i=="left":
#             answer[0] -= 1
#             if answer[0] < -(board[0]//2):
#                 answer[0] += 1
#         elif i=="right":
#             answer[0] += 1
#             if answer[0] > board[0]//2:
#                 answer[0] -= 1
#         elif i=="up":
#             answer[1] += 1
#             if answer[1] > board[1]//2:
#                 answer[1] -= 1
#         elif i=="down":
#             answer[1] -= 1
#             if answer[1] < -(board[1]//2):
#                 answer[1] += 1
#     return answer

def solution(keyinput, board):
    x_lim,y_lim = board[0]//2,board[1]//2
    move = {'left':[-1,0],'right':[1,0],'up':[0,1],'down':[0,-1]}
    x,y = 0,0
    for k in keyinput:
        dx,dy = move[k]
        if abs(x+dx)>x_lim or abs(y+dy)>y_lim:
            continue
        else:
            x,y = x+dx,y+dy

    return [x,y]

# 최댓값 만들기 (2)
def solution(numbers):
    return max(sorted(numbers)[0]*sorted(numbers)[1], sorted(numbers)[-1]*sorted(numbers)[-2])

# 다항식 더하기
def solution(polynomial):    
    a,b = 0,0
    for i in polynomial.split(" + "):
        if i.isdigit():
            b += int(i)  
        else:
            if i.isalpha():
                a += 1
            else:
                a += int(i[:-1])
    
    if a==1:
        a=''
    
    answer = f"{a}x + {b}"
    
    if answer.startswith("0"):
        return f"{b}"
    elif answer.endswith("0"):
        return f"{a}x"
    else:
        return answer
