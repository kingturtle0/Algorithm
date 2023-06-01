import sys

lines = sys.stdin.readlines()

for line in lines:
    A, B = map(int, line.split())
    if A and B:
        print(A + B)