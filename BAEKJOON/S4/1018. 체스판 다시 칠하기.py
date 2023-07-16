import sys
input = sys.stdin.readline

def paint(si, sj):
    w_cnt, b_cnt = 0, 0
    for i in range(si, si + 8):
        for j in range(sj, sj + 8):
            if (i + j) % 2 == 0:
                if arr[i][j] != 'B':
                    b_cnt += 1
                else:
                    w_cnt += 1
            else:
                if arr[i][j] != 'W':
                    b_cnt += 1
                else:
                    w_cnt += 1

    return min(b_cnt, w_cnt)


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

ans = 33
for i in range(N - 7):
    for j in range(M - 7):
        ans = min(ans, paint(i, j))

print(ans)