alphabet = [0] * 26
while True:
    try:
        for s in input():
            if s.isalpha():
                alphabet[ord(s) - ord('a')] += 1
    except EOFError:
        break

max_cnt = max(alphabet)
for i in range(26):
    if alphabet[i] == max_cnt:
        print(chr(i + ord('a')), end='')