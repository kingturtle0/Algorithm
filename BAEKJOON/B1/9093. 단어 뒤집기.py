T = int(input())
for _ in range(T):
    words = list(input().split())
    new_words = []
    for word in words:
        new_words.append(word[::-1])

    print(' '.join(new_words))