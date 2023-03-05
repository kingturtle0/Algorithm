C, R = map(int, input().split())
K = int(input())

if K > C*R:
    print(0)
else:
    direct = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    arr = [[1]*(C+2)] + [[1] + [0]*C + [1] for _ in range(R)] + [[1]*(C+2)]

    ci = cj = 1
    dr = 0
    for n in range(1, K):
        arr[ci][cj] = n
        ni, nj = ci + direct[dr][0], cj + direct[dr][1]
        if arr[ni][nj] == 0:
            ci, cj = ni, nj
        else:
            dr = (1 + dr) % 4
            ci, cj = ci + direct[dr][0], cj + direct[dr][1]

    print(cj, ci)