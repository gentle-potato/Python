print('#11번')
def mul() :
    x = int(input('숫자1 입력 : '))
    y = int(input('숫자2 입력 : '))
    mul = x * y
    return mul

print('두 수를 곱한 값은 %d' % mul())

print('\n=======================\n')

print('#12번')
def up() :
    a = input('문자 입력 : ')
    upper = a.upper()
    return upper

print('대문자로 변환하면 %s' % up())

print('\n=======================\n')

print('#13번')
def pickup_even(numbers) :
    even = []
    for number in numbers :
        if number % 2 == 0 :
            even.append(number)
        else :
            pass
    return even

list_ex = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 35, 50]
print(pickup_even(list_ex))