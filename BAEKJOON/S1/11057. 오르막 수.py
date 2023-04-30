N = int(input())

arr = [0] * (N + 1)

numbers = [1]*10
for i in range(1, N + 1):
    arr[i] = sum(numbers)
    for j in range(1, 10):
        numbers[j] += numbers[j - 1]

print(arr[N] % 10007)