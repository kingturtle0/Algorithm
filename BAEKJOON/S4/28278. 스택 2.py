import sys
input = sys.stdin.readline

stack = []
for _ in range(int(input())):
    commands = list(map(int, input().split()))
    if commands[0] == 1:
        stack.append(commands[1])
    elif commands[0] == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif commands[0] == 3:
        print(len(stack))
    elif commands[0] == 4:
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)
