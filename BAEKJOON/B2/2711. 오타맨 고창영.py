T = int(input())
for _ in range(T):
    n, word = input().split()
    print(''.join([word[i] for i in range(len(word)) if i != int(n) - 1]))