import sys

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

good_number_cnt = 0
for number in numbers:
    start = 0
    end = N - 1
    while start < end:
        if numbers[start] + numbers[end] == number:
            if numbers[start] != number and numbers[end] != number:
                good_number_cnt += 1
                break
            elif numbers[start] == number:
                start += 1
            elif numbers[end] == number:
                end -= 1
        elif numbers[start] + numbers[end] < number:
            start += 1
        else:
            end -= 1

print(good_number_cnt)