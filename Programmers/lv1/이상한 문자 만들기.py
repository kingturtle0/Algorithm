def solution(s):
    answer = []
    words = s.split(' ')
    for word in words:
        new_word = ''
        for i in range(len(word)):
            if i % 2:
                new_word += word[i].lower()
            else:
                new_word += word[i].upper()
        answer.append(new_word)
    return ' '.join(answer)