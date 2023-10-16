aeiou = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:
    engs = input()
    if engs == '#':
        break

    ans = 0
    for eng in engs:
        if eng in aeiou:
            ans += 1

    print(ans)
