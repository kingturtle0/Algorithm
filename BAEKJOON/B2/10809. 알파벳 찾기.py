S = input()
print(*[S.find(chr(i+ord('a'))) for i in range(26)])