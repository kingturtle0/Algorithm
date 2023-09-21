N = int(input())
alphabet = [0]*26
for _ in range(N):
    last_name = input()[0]
    alphabet[ord(last_name) - ord('a')] += 1

ans = ''
for i in range(26):
    if alphabet[i] >= 5:
        ans += chr(i + ord('a'))

if ans:
    print(ans)
else:
    print('PREDAJA')