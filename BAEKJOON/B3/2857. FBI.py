result = []
for i in range(1, 6):
    name = input()
    if 'FBI' in name:
        result.append(i)

if result:
    print(*result)
else:
    print('HE GOT AWAY!')