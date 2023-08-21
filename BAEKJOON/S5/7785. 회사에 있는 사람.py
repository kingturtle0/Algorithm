import sys
input = sys.stdin.readline

n = int(input())
logs = dict()
for _ in range(n):
    name, state = input().split()
    if state == 'enter':
        logs[name] = 1
    else:
        logs[name] = 0

for key, value in sorted(logs.items(), reverse=True):
    if value:
        print(key)