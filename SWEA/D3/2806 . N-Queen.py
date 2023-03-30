def check(ci, cj):
    for di, dj in ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)):
        ni, nj = ci + di, cj + dj
        while 0 <= ni < N and 0 <= nj < N:
            if arr[ni][nj]:
                return False

            ni, nj = ni + di, nj + dj

    return True


def backt(i):
    global answer
    if i == N:
        answer += 1
        return

    for j in range(N):
        if check(i, j):
            arr[i][j] = 1
            backt(i + 1)
            arr[i][j] = 0


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    answer = 0
    backt(0)

    print(f'#{test_case}', answer)
