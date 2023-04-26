N = int(input())

star = [' ' for _ in range(N)]
for i in range(N - 1, -1, -1):
    star[i] = '*'
    print(''.join(star))