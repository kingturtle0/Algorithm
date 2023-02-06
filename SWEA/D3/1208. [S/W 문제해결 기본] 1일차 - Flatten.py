for test_case in range(1, 11):
    dump_count = int(input())
    boxes = list(map(int, input().split()))

    while dump_count > 0:
        max_val, min_val = boxes[0], boxes[0]
        max_idx, min_idx = 0, 0
        for i in range(1, 100):
            if max_val < boxes[i]:
                max_val = boxes[i]
                max_idx = i
            elif boxes[min_idx] > boxes[i]:
                min_val = boxes[i]
                min_idx = i

        if max_val - min_val > 1:
            boxes[max_idx] -= 1
            boxes[min_idx] += 1
            dump_count -= 1
        else:
            break
	
    max_val, min_val = boxes[0], boxes[0]
    for i in range(1, 100):
        if max_val < boxes[i]:
            max_val = boxes[i]
        elif boxes[min_idx] > boxes[i]:
            min_val = boxes[i]
    
    result = max_val - min_val

    print(f'#{test_case}', result)