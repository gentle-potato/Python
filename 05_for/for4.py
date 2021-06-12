# 2 ~ 9단 구구단 출력

for dan in range(2, 10) :
    for n in range(1, 10) :
        print('%d * %d = %2d' % (dan, n, dan * n))
    
    print()