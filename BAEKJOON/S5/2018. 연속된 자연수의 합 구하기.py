N = int(input())
start = 1
end = 1

cnt = 1
total = 1
while end != N:
    if total > N:
        total -= start
        start += 1
    elif total < N:
        end += 1
        total += end
    else:
        cnt += 1
        end += 1
        total += end

print(cnt)