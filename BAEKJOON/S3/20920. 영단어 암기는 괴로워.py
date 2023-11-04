import sys

N, M = map(int, input().split())
words = dict()
for _ in range(N):
    word = sys.stdin.readline().rstrip()
    if len(word) < M:
        continue
    else:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

results = sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for result in results:
    print(result[0])
