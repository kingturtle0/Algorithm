T = int(input())

result = []
for i in range(1, T + 1):
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        result.append('-'*(str(i).count('3')+str(i).count('6')+str(i).count('9')))
    else:
        result.append(str(i))
        
for i in result:
    print(i, end = ' ')
