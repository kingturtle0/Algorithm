A, B, C = map(int, input().split())
benefit = C - B
if benefit > 0:
    ans = A // benefit + 1
else:
    ans = -1
print(ans)