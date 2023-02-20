T = int(input())

def win(i, j):
    if i == j:
        return i

    player1 = win(i, (i + j)//2)
    player2 = win((i + j)//2 + 1, j)

    if lst[player1] == 1:
        if lst[player2] == 2:
            return player2
        else:
            return player1
    elif lst[player1] == 2:
        if lst[player2] == 3:
            return player2
        else:
            return player1
    else:
        if lst[player2] == 1:
            return player2
        else:
            return player1

for test_case in range(1, T + 1):
    N = int(input())
    lst = [0] + list(map(int, input().split()))

    ans = win(1, N)
    print(f'#{test_case}', ans)