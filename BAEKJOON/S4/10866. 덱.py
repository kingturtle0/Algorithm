import sys
input = sys.stdin.readline

N = int(input())
deque = []
for _ in range(N):
    command = input().split()
    if command[0] == "push_front":
        deque.insert(0, command[1])
    elif command[0] == "push_back":
        deque.append(command[1])
    elif command[0] == "pop_front":
        if deque:
            ans = deque.pop(0)
        else:
            ans = -1
        print(ans)
    elif command[0] == "pop_back":
        if deque:
            ans = deque.pop()
        else:
            ans = -1
        print(ans)
    elif command[0] == "size":
        print(len(deque))
    elif command[0] == "empty":
        if deque:
            ans = 0
        else:
            ans = 1
        print(ans)
    elif command[0] == "front":
        if deque:
            ans = deque[0]
        else:
            ans = -1
        print(ans)
    elif command[0] == "back":
        if deque:
            ans = deque[-1]
        else:
            ans = -1
        print(ans)