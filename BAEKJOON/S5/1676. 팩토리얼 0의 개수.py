N = int(input())
num = 1
while N > 1:
    num *= N
    N -= 1

ans = 0
for n in str(num)[::-1]:
    if n == "0":
        ans += 1
    else:
        break

print(ans)