M = int(input())
N = int(input())
numbers = [i**2 for i in range(101, 0, -1)]
ans, min_ans = 0, 0
for number in numbers:
    if M <= number <= N:
        ans += number
        min_ans = number

if ans:
    print(ans, min_ans, sep='\n')
else:
    print(-1)