for _ in range(int(input())):
    N, *scores = map(int,input().split())
    mean = sum(scores) / N
    cnt = 0
    for score in scores:
        if score > mean:
            cnt += 1
    
    print(f'{cnt/N*100:0.3f}%')