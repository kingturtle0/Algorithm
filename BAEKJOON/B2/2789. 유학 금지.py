words = input()
lst = list('CAMBRIDGE')
ans = ''
for word in words:
    if word not in lst:
        ans += word
print(ans)
