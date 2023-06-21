while True:
    N = input()
    if N == "0":
        break
    ans = "yes" if N == N[::-1] else "no"
    print(ans)
