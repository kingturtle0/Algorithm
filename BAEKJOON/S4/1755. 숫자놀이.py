num_dict = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
               5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', }
M, N = map(int, input().split())
sorted_numbers = sorted([(n, ''.join([num_dict[int(n)] for n in str(n)]), ) for n in range(M, N + 1)], key=lambda x: x[1])
for i in range(len(sorted_numbers)):
    print(sorted_numbers[i][0], end=' ')
    if i % 10 == 9:
        print()
