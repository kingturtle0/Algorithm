A, B = map(int, input().split())
numbers = [0]
for i in range(1, 1001):
    for j in range(i):
        numbers.append(i)

print(sum(numbers[A:B+1]))