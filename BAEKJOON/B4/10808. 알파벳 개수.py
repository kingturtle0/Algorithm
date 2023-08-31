S = input()
alphabet = [0]*26
for s in S:
    alphabet[ord(s) - ord('a')] += 1

print(*alphabet)