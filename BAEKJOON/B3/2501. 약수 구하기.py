N, K = map(int, input().split())
numbers = []

m = 1
while N >= m:
    if N % m == 0:
        numbers.insert(0, N // m)
    m += 1

if K > len(numbers):
    print(0)
else:
    print(numbers[K - 1])