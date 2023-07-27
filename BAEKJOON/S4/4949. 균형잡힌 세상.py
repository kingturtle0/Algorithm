import sys

input = sys.stdin.readline


def check(s, stack):
    for b in s:
        if b == '(':
            stack.append('(')
        elif b == '[':
            stack.append('[')
        elif b == ')':
            if stack:
                c = stack.pop()
                if c != '(':
                    return 'no'
            else:
                return 'no'
        elif b == ']':
            if stack:
                c = stack.pop()
                if c != '[':
                    return 'no'
            else:
                return 'no'

    if stack:
        return 'no'

    return 'yes'


while True:
    string = input().rstrip()
    if string == '.':
        break

    print(check(string, []))