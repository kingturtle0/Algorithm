import sys
input = sys.stdin.readline

N = int(input())
word_set = set()
for _ in range(N):
    word_set.add(input())

words = sorted(list(word_set), key=lambda x:(len(x), x))

for word in words:
    print(word, end='')