def solution(board, moves):
    answer = 0
    n = len(board)
    stack = []
    for move in moves:
        for i in range(n):
            doll = board[i][move - 1]
            if doll:
                board[i][move - 1] = 0
                if stack:
                    if stack[-1] != doll:
                        stack.append(doll)
                    else:
                        stack.pop()
                        answer += 2
                else:
                    stack.append(doll)
                break
    return answer