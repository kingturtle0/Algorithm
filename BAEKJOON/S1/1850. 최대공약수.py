A, B = map(int, input().split())

if A > B:
    A, B = B, A

while B:
    A, B = B, A % B

print('1'*A)