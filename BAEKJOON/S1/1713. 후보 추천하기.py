N = int(input())
M = int(input())
lst = list(map(int, input().split()))
result = []
cnt = [0]*101

time = 0
for i in range(M):
    num = lst[i]
    cnt[num] += 1
    length = len(result)

    if length < N:
        for j in range(length):
            if result[j][0] == num:
                result[j][1] = cnt[num]
                break
        else:
            result.append([num, cnt[num], time])
    else:
        for j in range(N):
            if result[j][0] == num:
                result[j][1] = cnt[num]
                break
        else:
            mn = min(result, key=lambda x:(x[1], x[2]))
            idx = result.index(mn)
            result[idx] = [num, cnt[num], time]
            cnt[mn[0]] = 0

    time += 1

result.sort(key=lambda x:x[0])
for ans in result:
    print(ans[0], end=" ")
