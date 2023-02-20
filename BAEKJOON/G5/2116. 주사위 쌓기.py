import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
max_val = -(21e8)

for i in range(6):
    num = i+1
    val = 0
    for j in range(N):
        for k in range(6):
            if arr[j][k] == num:
                if k == 0:
                    num = arr[j][5]
                    val += max(arr[j][1], arr[j][2], arr[j][3], arr[j][4])
                    break
                elif k == 1:
                    num = arr[j][3]
                    val += max(arr[j][0], arr[j][2], arr[j][4], arr[j][5])
                    break
                elif k == 2:
                    num = arr[j][4]
                    val += max(arr[j][0], arr[j][1], arr[j][3], arr[j][5])
                    break
                elif k == 3:
                    num = arr[j][1]
                    val += max(arr[j][0], arr[j][2], arr[j][4], arr[j][5])
                    break
                elif k == 4:
                    num = arr[j][2]
                    val += max(arr[j][0], arr[j][1], arr[j][3], arr[j][5])
                    break
                elif k == 5:
                    num = arr[j][0]
                    val += max(arr[j][1], arr[j][2], arr[j][3], arr[j][4])
                    break

    if max_val < val:
        max_val = val

print(max_val)