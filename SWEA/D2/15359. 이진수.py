T = int(input())

def htob(n):
    bin = ['0']*4
    idx = -1
    while n > 0:
        n, d = n // 2, n % 2
        bin[idx] = str(d)
        idx -= 1

    return ''.join(bin)

for test_case in range(1, T + 1):
    N, lst = input().split()
    N = int(N)
    lst = list(lst)

    ans = ''
    for i in range(N):
        if lst[i].isdigit():
            ans += htob(int(lst[i]))
        else:
            h = '1' + str(ord(lst[i])-ord('A'))
            ans += htob(int(h))

    print(f'#{test_case}', ans)