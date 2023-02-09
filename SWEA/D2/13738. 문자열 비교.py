T = int(input())

for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()

    def strLen(st):
        length = 0
        for s in st:
            length += 1
        return length

    str1len = strLen(str1)
    str2len = strLen(str2)

    def isMatch(idx):
        for i in range(str1len):
            if str2[idx+i] != str1[i]:
                return 0
        return 1

    flag = 0
    for i in range(str2len-str1len+1):
        if isMatch(i):
            flag = 1
            break

    print(f'#{test_case}', flag)