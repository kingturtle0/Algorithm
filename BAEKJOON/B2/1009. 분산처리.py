patterns = [[1], [2, 4, 8, 6], [3, 9, 7, 1], [4, 6], [5], [6], [7, 9, 3, 1], [8, 4, 2, 6], [9, 1], [10]]

for _ in range(int(input())):
    a, b = map(int, input().split())
    n = a % 10 - 1
    length = len(patterns[n])
    if length == 1:
        print(patterns[n][0])
    else:
        print(patterns[n][b % length - 1])