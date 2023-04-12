equation = input()
lst = equation.split('-')

ans = 0
if '+' in lst[0]:
    ans = sum(map(int, lst[0].split('+')))
else:
    ans = int(lst[0])

for i in range(1, len(lst)):
    if '+' in lst[i]:
        ans -= sum(map(int, lst[i].split('+')))
    else:
        ans -= int(lst[i])

print(ans)