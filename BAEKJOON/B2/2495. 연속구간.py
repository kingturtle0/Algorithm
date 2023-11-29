for _ in range(3):
    n = input()
    length = 1
    max_length = 1
    for i in range(1, 8):
        if n[i] == n[i - 1]:
            length += 1
            max_length = max(max_length, length)
        else:
            length = 1
    print(max_length)
