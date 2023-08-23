N = int(input())
numbers = sorted(list(map(int, input().split())))
if N > 1:
    print(numbers[0]*numbers[-1])
else:
    print(numbers[0]*numbers[0])