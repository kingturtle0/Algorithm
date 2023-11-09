a, b, c = map(int, input().split())
if a == b and b == c and c == a:
    print(10000 + 1000 * a)
elif a != b and b != c and c != a:
    print(max(a, b, c) * 100)
else:
    same = a
    if b == c:
        same = b
    print(1000 + same * 100)