N = int(input())
words = [list(input()) for _ in range(N)]
word = words[0]
word_len = len(word)
for i in range(1, N):
    temp = words[i]
    for j in range(word_len):
        if word[j] != temp[j]:
            word[j] = '?'

print(''.join(word))