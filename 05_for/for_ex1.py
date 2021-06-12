print('# 100까지의 합')
total_1 = 0

for i in range(1, 101) :
    total_1 += i

print('1 ~ 100 합 : %d' % total_1)

print('\n=====================\n')

# ==============================================

print('# 합계, 3의 배수 출력')
total_2 = 0

for n in range(3, 21, 3) :
    print(n, end = ' ')
    total_2 += n

print('\n1 ~ 20 중 3의 배수의 합 : %d' % total_2)

print('\n=====================\n')

# ==============================================

print('#range()의 step 인수를 사용하지 않고 구하기')

total_3 = 0

for x in range(1, 21) :
    if x % 3 == 0 :
        print(x, end = ' ')
        total_3 += x
print('\n1 ~ 20 중 3의 배수의 합 : %d' % total_3)

# 강사님 풀이
total_3 = 0

for y in [1, 2, 3, 4, 5, 6] :
    z = y * 3
    print(z, end = ' ')
    total_3 += z
print('\n1 ~ 20 중 3의 배수의 합 : %d' % total_3)