def makelst(arr): # 별, 동그라미, 네모, 세모 순서로 개수 리스트 만들기
    n, lst = arr[0], arr[1:] # 첫 번째가 총 개수, 두 번째부터 모양들
    ans = [0]*4
    for i in range(n):
        if lst[i] == 4:
            ans[0] += 1
        elif lst[i] == 3:
            ans[1] += 1
        elif lst[i] == 2:
            ans[2] += 1
        else:
            ans[3] += 1

    return ans

N = int(input())

for _ in range(N): # N만큼 반복
    # 플레이어1,2로 입력받고
    player1 = list(map(int, input().split()))
    player2 = list(map(int, input().split()))
    # 두 플레이어 모두 개수리스트 구하기
    lst1 = makelst(player1)
    lst2 = makelst(player2)

    # 우선순위가 높은 순으로 리스트를 만들었으므로
    # i 순대로 먼저 비교하고 승자 출력 후 종료
    # 또는 리스트 전체가 같다면 무승부 출력 후 종료
    for i in range(4): 
        if lst1 == lst2:
            print('D')
            break

        if lst1[i] > lst2[i]:
            print('A')
            break
        elif lst1[i] < lst2[i]:
            print('B')
            break