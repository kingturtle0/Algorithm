A, B, C = map(int, input().split())
a, b, c, d = (A + B) % C, ((A % C) + (B % C)) % C, (A * B) % C, ((A % C) * (B % C)) % C
print(a, b, c, d, sep='\n')