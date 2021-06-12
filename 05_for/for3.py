# 다중 for(중첩 for)
for i in range(4) :
    for j in range(5) :
        print(j, end = ' ')

    print()

print('\n-----------------\n')

# 연습문제
for x in range(3) :
    for y in range(1, 5) :
        # print('%2s' % (4 * x + y), end = ' ')
        print(4 * x + y, end='\t')

    print()

print('# 또는')
n = 0
for a in range(3) :
    for b in range(1, 5) :
        n += 1
        # print('%2s' % (4 * x + y), end = ' ')
        print(4 * a + b, end='\t')

    print()