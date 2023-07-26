N = int(input())

six, ans = 1, 1
while N > six:
    six += 6 * ans
    ans += 1

print(ans)