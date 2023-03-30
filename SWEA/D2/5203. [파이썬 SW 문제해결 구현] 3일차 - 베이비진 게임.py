def win(lst):
    for i in range(10):
        if lst[i] == 3:
            return True

    for i in range(8):
        if lst[i] and lst[i + 1] and lst[i + 2]:
            return True

    return False

T = int(input())

for test_case in range(1, T + 1):
    cards = list(map(int, input().split()))

    player1 = [0]*10
    player2 = [0]*10
    ans = 0
    idx = 0
    while idx < 12:
        if idx % 2 == 0:
            player1[cards[idx]] += 1
        else:
            player2[cards[idx]] += 1

        if win(player1):
            ans = 1
            break

        if win(player2):
            ans = 2
            break

        idx += 1

    print(f'#{test_case}', ans)