S = ''
while True:
    try:
       S += input()
    except EOFError:
        break

print(sum(map(int, S.split(','))))
