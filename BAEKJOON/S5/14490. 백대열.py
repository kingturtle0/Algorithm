n, m = map(int, input().split(':'))
y, x = max(n, m), min(n, m)
while True:
    y, x = x, y % x
    if x == 0:
        print(f'{n // y}:{m // y}')
        break