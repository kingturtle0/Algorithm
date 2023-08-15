import sys
input = sys.stdin.readline

N = int(input())
my = dict()
for n in map(int, input().split()):
    my[n] = 1
M = int(input())
for m in map(int, input().split()):
    if my.get(m) == 1:
        ans = 1
    else:
        ans = 0
    print(ans, end=" ")