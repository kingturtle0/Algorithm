while True:
    try:
        string = input()
        result = [0]*4
        for s in string:
            if s.islower():
                result[0] += 1
            elif s.isupper():
                result[1] += 1
            elif s.isspace():
                result[3] += 1
            else:
                result[2] += 1

        print(*result)
    except EOFError:
        break