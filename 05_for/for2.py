for i in range(10) :   # 0부터 9까지(START 값을 지정하지 않으면 0)
    print(i, end = ' ')

print('\n-------------')

for i in range(1, 10) :   # 1부터 9까지(STOP 값은 포함X)
    print(i, end=' ')

print('\n-------------')

for i in range(2, 10, 2) :   # 10을 포함하고 싶으면 가운데 STOP 값을 11로 하면 됨
    print(i, end=' ')

print('\n-------------')

for i in range(12, 1, -1) :
    print(i, end=' ')

print('\n-------------')


# 1 ~ 10 사이의 수를 더하고 더한 결과 출력

total_1 = 0   # 누적변수가 반드시 초기화되어 있어야 함!
total_2 = 0

for n in range(11) :
    total_1 = total_1 + n
print('합은 %d ' % total_1)

for i in range(11) :
    total_2 += i
print('합은 %d ' % total_2)