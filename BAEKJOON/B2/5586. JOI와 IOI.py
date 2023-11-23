s = input()
n = len(s)
JOI, IOI = 0, 0
for i in range(2, n):
    if s[i - 2:i + 1] == 'JOI':
        JOI += 1
    elif s[i - 2:i + 1] == 'IOI':
        IOI += 1
print(JOI)
print(IOI)