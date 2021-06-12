print('#1')
print('1)')

for j in range(5, 0, -1) :
    for i in range(j) :
        print('*', end = '')   # j만큼 *을 옆으로 나열!
    print()

print('\n2)')

for y in range(5, 0, -1) :
    for x in range(y) :
        print(' ', end = '')
    for x in range(y) :
        print('*' * (2 * x - 1), end = '')

print('\n========================\n')

print('#2')
num = int(input('숫자 입력 : '))
while True :
    if num == 7 :
        print(num, '입력! 종료')
        break
    else :
        num = int(input('다시 입력 : '))
