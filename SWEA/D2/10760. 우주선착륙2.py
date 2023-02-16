T = int(input())

def isCandidate(y, x, dr1, dr2, arr):
    cnt = 0
    for i in range(8):
        dy = y + dr1[i]
        dx = x + dr2[i]

        if 0 <= dy < N and 0 <= dx < M:
            if arr[dy][dx] < arr[y][x]:
                cnt += 1

    if cnt >= 4:
        return 1

    return 0

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    directi = [-1, -1, -1, 0, 0, 1, 1, 1]
    directj = [-1, 0, 1, -1, 1, -1, 0, 1]

    candidate_cnt = 0
    for i in range(N):
        for j in range(M):
            if isCandidate(i, j, directi, directj, arr):
                candidate_cnt += 1

    print(f'#{test_case}', candidate_cnt)