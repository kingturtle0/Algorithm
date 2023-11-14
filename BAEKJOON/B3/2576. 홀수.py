odds = []
for _ in range(7):
    n = int(input())
    if n % 2:
        odds.append(n)
if odds:
    print(sum(odds), min(odds), sep='\n')
else:
    print(-1)