numbers = [int(input()) for _ in range(5)]
avg = sum(numbers) // 5
mid = sorted(numbers)[2]
print(avg, mid, sep='\n')
