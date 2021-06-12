# 1부터 100까지의 모든 3의 배수의 합 계산
n = 1
total = 0

while n <= 100 :
    if n % 3 == 0 :
        total += n
    n += 1

print('1부터 100까지 모든 3의 배수의 합은 %d입니다.' % total)

print('\n# 또는\n')

n = 0
total = 0

while n <= 100 :
    total += n
    n += 3

print('1부터 100까지 모든 3의 배수의 합은 %d입니다.' % total)

print('\n# 또는\n')

n = 1
total = 0

while n * 3 <= 100 :   # 3의 배수만 나옴
    total += n * 3
    n += 1

print('1부터 100까지 모든 3의 배수의 합은 %d입니다.' % total)