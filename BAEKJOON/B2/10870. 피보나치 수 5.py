fib = [0, 1] + [0] * 19
for i in range(2, 21):
    fib[i] = fib[i - 1] + fib[i - 2]
print(fib[int(input())])