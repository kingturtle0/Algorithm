T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    arr = [[0 for _ in range(N+2)] for _ in range(N+2)]
    for i in range(N//2, N//2+2):
        for j in range(N//2, N//2+2):
            if i == j:
                arr[i][j] = 2
            else:
                arr[i][j] = 1

    for _ in range(M):
        si, sj, c = map(int, input().split())
        arr[si][sj] = c

        for di, dj in ((-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)):
            flips = []
            for cnt in range(1, N):
                ni = si + di*cnt
                nj = sj + dj*cnt
                if arr[ni][nj] == 0:
                    break
                elif arr[ni][nj] != c:
                    flips.append((ni, nj))
                elif arr[ni][nj] == c:
                    while flips:
                        i, j = flips.pop()
                        arr[i][j] = c
                    break

    black = white = 0
    for i in range(N+2):
        for j in range(N+2):
            if arr[i][j] == 1:
                black += 1
            elif arr[i][j] == 2:
                white += 1

    print(f'#{test_case}', black, white)