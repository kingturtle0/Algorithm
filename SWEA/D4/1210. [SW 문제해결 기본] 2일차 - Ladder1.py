for test_case in range(10):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    goal = 0
    for j in range(100):
        if arr[99][j] == 2:
            goal = j

    directx = [-1, 1]
    for i in range(99, -1, -1):
        for x in directx:
            dx = goal + x
            if 0 <= dx < 100 and arr[i][dx]:
                while True:
                    if 0 <= dx < 100 and arr[i][dx]:
                        dx += x
                    else:
                        break
                goal = dx - x
                break

    print(f"#{T}", goal)