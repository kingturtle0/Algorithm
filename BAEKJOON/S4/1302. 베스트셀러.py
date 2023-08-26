N = int(input())
books = dict()
for _ in range(N):
    book = input()
    if book in books:
        books[book] += 1
    else:
        books[book] = 1

best_sellers = []
max_value = 0
for value in books.values():
    max_value = max(max_value, value)

for key, value in books.items():
    if value == max_value:
        best_sellers.append(key)

best_sellers.sort()
print(best_sellers[0])
