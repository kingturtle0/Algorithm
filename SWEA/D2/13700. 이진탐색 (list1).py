T = int(input())

for test_case in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())

    def FindPageCount(left, right, target):
        cnt = 0
        while True:
            center = int((left + right)/2)
            if target > center:
                left = center
            elif target < center:
                right = center
            else:
                break
            cnt += 1

        return cnt

    cnt_Pa = FindPageCount(1, P, Pa)
    cnt_Pb = FindPageCount(1, P, Pb)

    if cnt_Pa < cnt_Pb:
        result = 'A'
    elif cnt_Pa > cnt_Pb:
        result = 'B'
    else:
        result = 0

    print(f'#{test_case}', result)