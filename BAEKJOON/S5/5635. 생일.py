n = int(input())
birthdays = [input().split() for _ in range(n)]
birthdays.sort(key=lambda x: [-int(x[3]), -int(x[2]), -int(x[1])])
print(birthdays[0][0])
print(birthdays[-1][0])