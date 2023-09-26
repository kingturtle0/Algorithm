while True:
    secret = input()
    if secret == 'END':
        break
    print(secret[::-1])