N = int(input())
for _ in range(N):
    sentence = list(input())
    sentence[0] = sentence[0].upper()
    print(''.join(sentence))