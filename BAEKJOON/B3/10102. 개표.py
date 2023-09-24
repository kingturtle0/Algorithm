V = int(input())
result = input()
a, b = result.count('A'), result.count('B')
if a > b:
    print('A')
elif a < b:
    print('B')
else:
    print('Tie')