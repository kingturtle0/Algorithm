bowls = input()
ans = 0
prev = ''
for bowl in bowls:
    if bowl == prev:
        ans += 5
    else:
        ans += 10
    prev = bowl

print(ans)