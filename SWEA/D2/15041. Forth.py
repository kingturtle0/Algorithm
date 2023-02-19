T = int(input())

def forth(lst):
    stack = []
    for i in range(len(lst)):
        if lst[i] == '.':
            if len(stack) == 1:
                return stack.pop()
            else:
                return 'error'
        elif len(stack) < 2:
            if lst[i] == '+' or lst[i] == '-' or lst[i] == '*' or lst[i] == '/':
                return 'error'
            else:
                stack.append(int(lst[i]))
        else:
            if lst[i] == '+':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 + num1)
            elif lst[i] == '-':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)
            elif lst[i] == '*':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 * num1)
            elif lst[i] == '/':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 // num1)
            else:
                stack.append(int(lst[i]))

for test_case in range(1, T + 1):
    lst = list(input().split())

    print(f'#{test_case} {forth(lst)}')
