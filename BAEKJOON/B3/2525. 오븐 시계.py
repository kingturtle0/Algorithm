A, B = map(int, input().split())
C = int(input())
h, m = C // 60, C % 60
A += h
B += m
if B >= 60:
    B -= 60
    A += 1

if A >= 24:
    A -= 24

print(A, B)
