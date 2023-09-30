N = input()
n = len(N)
if sum(map(int, N[:n//2])) == sum(map(int, N[n//2:])):
    print('LUCKY')
else:
    print('READY')