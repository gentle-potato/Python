#1 for문 코드 작성
print('#1 for문 코드 작성')

print('1)')
for i in range(5) :
    print('*' * (5 - i))

print('\n2)')
for j in range(1, 6) :
    star = '*' * (2 * j - 1)
    print(f'{star : ^9s}')

print('\n========================\n')

#2 7 입력! 종료
print('#2 7 입력! 종료')

num = int(input('숫자 입력 : '))

while num != 7 :
    num = int(input('다시 입력 : '))
    if num == 7 :
        break

print('7 입력! 종료')

print('\n========================\n')

#3 노래방 기계 무한 반복
print('#3 노래방 기계 무한 반복')

money = 10000 ; remain = 10000

for x in range(1, 6) :
    if remain > 0 :
        song = x
        remain = money - 2000 * song
        print(f'노래를 {song}곡 불렀습니다.\n현재 {remain}원 남았습니다.')

print('잔액이 없습니다. 종료합니다.')