import sys
input = sys.stdin.readline

N = int(input())
numbers = [int(input()) for _ in range(N)]
num_dic = {number: 0 for number in numbers}
for number in numbers:
    num_dic[number] += 1

cnt = 0
for value in num_dic.values():
    cnt = max(cnt, value)

modes = []
for key, value in num_dic.items():
    if value == cnt:
        modes.append(key)

mean = round(sum(numbers)/N)
median = sorted(numbers)[N//2]
mode = sorted(modes)[1] if len(modes) > 1 else modes[0]
rng = max(numbers) - min(numbers)

print(mean, median, mode, rng, sep="\n")