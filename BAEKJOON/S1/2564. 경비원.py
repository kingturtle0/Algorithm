row, col = map(int, input().split())

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
ta, tb = map(int, input().split())

ans = 0
for i in range(N):
    if ta == lst[i][0]:   # 동서남북이 같으면
        ans += abs(tb - lst[i][1]) # 거리만 재기
    else: # 동서남북이 다를 때는
        if ta == 1:  #가까운 쪽으로 거리를 구하도록 모든 조건을 추가
            if lst[i][0] == 2:
                if tb + lst[i][1] > row:
                    ans += col + (row - tb) + (row - lst[i][1])
                else:
                    ans += col + tb + lst[i][1]
            elif lst[i][0] == 3:
                ans += tb + lst[i][1]
            elif lst[i][0] == 4:
                ans += (row - tb) + lst[i][1]
        elif ta == 2:
            if lst[i][0] == 1:
                if tb + lst[i][1] > row:
                    ans += col + (row - tb) + (row - lst[i][1])
                else:
                    ans += col + tb + lst[i][1]
            elif lst[i][0] == 3:
                ans += tb + (col - lst[i][1])
            elif lst[i][0] == 4:
                ans += (row - tb) + (col - lst[i][1])
        elif ta == 3:
            if lst[i][0] == 1:
                ans += tb + lst[i][1]
            elif lst[i][0] == 2:
                ans += (col - tb) + lst[i][1]
            elif lst[i][0] == 4:
                if tb + lst[i][1] > col:
                    ans += row + (col - tb) + (col - lst[i][1])
                else:
                    ans += row + tb + lst[i][1]
        else:
            if lst[i][0] == 1:
                ans += tb + (row - lst[i][1])
            elif lst[i][0] == 2:
                ans += (col - tb) + (row - lst[i][1])
            elif lst[i][0] == 3:
                if tb + lst[i][1] > col:
                    ans += row + (col - tb) + (col - lst[i][1])
                else:
                    ans += row + tb + lst[i][1]

print(ans)