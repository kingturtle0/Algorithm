word = list(input().upper())

ans = 0
alst = list(set(word))
lst = []
for s in alst:
    lst.append(word.count(s))

mx = max(lst)
if lst.count(mx) > 1:
    print('?')
else:
    print(alst[lst.index(mx)])