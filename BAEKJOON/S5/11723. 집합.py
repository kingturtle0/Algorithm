import sys

input = sys.stdin.readline

S = [0]*21
N = int(input())
for _ in range(N):
    command = input().split()
    x = 0
    if len(command) > 1:
        c, x = command[0], int(command[1])
    else:
        c = command[0]

    if c == "add":
        if S[x] == 0:
            S[x] = 1
    elif c == "remove":
        if S[x] == 1:
            S[x] = 0
    elif c == "check":
        if S[x] == 1:
            print(1)
        else:
            print(0)
    elif c == "toggle":
        if S[x] == 1:
            S[x] = 0
        else:
            S[x] = 1
    elif c == "all":
        S = [1]*21
    else:
        S = [0]*21