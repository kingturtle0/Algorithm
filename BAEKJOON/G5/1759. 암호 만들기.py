def check(char):
    cnts = [0] * 5
    for i in range(5):
        cnts[i] = char.count(aeiou[i])

    if sum(cnts) == 0:
        return False
    elif sum(cnts) > (L - 2):
        return False

    return True


def solve(n, ans, st):
    if n == L:
        if check(ans):
            print(''.join(ans))
        return

    for i in range(st, C):
        solve(n + 1, ans + lst[i], i + 1)


L, C = map(int, input().split())
lst = sorted(list(input().split()))
aeiou = ['a', 'e', 'i', 'o', 'u']

solve(0, '', 0)