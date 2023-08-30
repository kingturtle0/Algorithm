word = input()
n = len(word)
for i in range(0, n, 10):
    print(word[i:i+10])
