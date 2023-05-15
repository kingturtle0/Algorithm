A = int(input())
B = int(input())
C = int(input())
ans = str(A * B * C)
result = [0] * 10

for n in ans:
    result[int(n)] += 1

for i in range(10):
    print(result[i])