bingo = [list(map(int, input().split())) for _ in range(5)]
tbingo = list(map(list, zip(*bingo))) # 뒤집은 빙고판
numbers = [list(map(int, input().split())) for _ in range(5)]

def is3Bingo(arr1, arr2): # 빙고가 3개인지
    cnt = 0
    for i in range(5):
        cnt1, cnt2 = 0, 0
        for j in range(5):
            if arr1[i][j] == -1:
                cnt1 += 1

            if arr2[i][j] == -1:
                cnt2 += 1
        if cnt1 == 5:
            cnt += 1
        if cnt2 == 5:
            cnt += 1

    cnt3, cnt4 = 0, 0
    for i in range(5):
        if arr1[i][i] == -1:
            cnt3 +=1

        if arr1[i][4-i] == -1:
            cnt4 += 1

    if cnt3 == 5:
        cnt += 1
    if cnt4 == 5:
        cnt += 1

    if cnt >= 3:
        return 1

    return 0

ans = flag = 0
for i in range(5):
    for j in range(5):
        ans += 1
        val = numbers[i][j]
        for y in range(5):     # 빙고판에 부른 숫자를 -1로 바꿔주고
            for x in range(5):
                if bingo[y][x] == val:
                    bingo[y][x] = -1

                if tbingo[y][x] == val:
                    tbingo[y][x] = -1

        if is3Bingo(bingo, tbingo): # 계속 빙고가 3개가 나오는지 확인
            flag = 1
            break

    if flag == 1:
        break

print(ans) # 출력