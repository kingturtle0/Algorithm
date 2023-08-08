lst = [1]*10001

idx = 1
while True:
    if lst[idx]:
        n = idx
        while True:
            for s in str(n):
                n += int(s)
            if n > 10000:
                break
            lst[n] = 0
    idx += 1
    if idx > 10000:
        break

for i in range(1, 10001):
    if lst[i]:
        print(i)