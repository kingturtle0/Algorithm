T = int(input())

for test_case in range(1, T + 1):
    date = input()
    year, month, day = int(date[:4]), int(date[4:6]), int(date[6:])
    limit = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    if (0 < month <= 12) and (0 < day <= limit[month]):
        print(f"#{test_case} %04d/%02d/%02d" % (year, month, day))
    else:
        print(f"#{test_case} -1")
