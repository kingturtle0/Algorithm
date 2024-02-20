def solution(n, words):
    dic = dict()
    for idx, word in enumerate(words):
        if word in dic:
            return [idx % n + 1, idx // n + 1]
        else:
            if idx and word[0] != words[idx - 1][-1]:
                return [idx % n + 1, idx // n + 1]
            else:
                dic[word] = 1
    return [0, 0]