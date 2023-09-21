A = input()
oper = input()
B = input()

if oper == '*':
    ans = '1' + '0'*(len(A) + len(B) - 2)
else:
    ans = int(A) + int(B)

print(ans)