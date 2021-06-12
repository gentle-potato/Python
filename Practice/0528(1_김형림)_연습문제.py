print('<1.>')
f = lambda x, y : x ** y
print('f = lambda x, y : x ** y')

print('\n====================\n')

print('<2.>')
ex = [1, 2, 3, 4, 5]
list(map(lambda x : x ** 2, ex))
print('list(map(lambda x : x ** 2, ex))')

print('\n====================\n')

print('<3.>')
print('3번 : 개별 .py 파일은 모듈이다.')

print('\n====================\n')

print('<4.>')
print('3번 __init__.py')

print('\n====================\n')

print('<5.>')
print('2번 import os as * : 와일드카드가 별칭으로 들어가서...?')

print('\n====================\n')

print('<6.>')
print('import fah_converter as fah')
import fah_converter as fah
print("Enter a celsius value: ")
celsius = float(input())
fahrenheit = fah.covert_c_to_f(celsius)
print("That's ", fahrenheit, " degrees Fahrenheit")
print('import fah_converter as fah')

print('\n====================\n')

print('<7.>')
print('from game.graphic.render import render_test()')

# print('\n====================\n')
#
# print('<8.>')
# f = open("hello_python.txt", 'a')
# f.write('hello, python!')
# print('(가) : a, (나) : write')   ##########

print('\n====================\n')

print('<9.>')
print('(가) 쓰기 모드 : w\n(나) 추가 모드 : a\n(다) 읽기 모드 : r')

print('\n====================\n')

print('<10.>')
print('from calculator import *')

print('\n====================\n')

print('<11.>')
print('--- 예측 ---')
print('7\n3\n2\n1\n1\n1\n종료되었습니다.')
print('--- 결과 ---')
try:
    for i in range(1, 7):
        result = 7 // i
        print(result)
except ZeroDivisionError:
    print("Not divided by 0")
finally:
    print("종료되었습니다.")

print('\n====================\n')

print('<12.>')
sentence = list("Hello Gachon")
print('--- 예측 ---')
print('5번 pop from empty list')
print('--- 결과 ---')
while (len(sentence) + 1):
    try:
        print(sentence.pop(0))
    except Exception as e:
        print(e)
        break

print('\n====================\n')

print('<13.>')
print('4번 IndexError, ValueError')

print('\n====================\n')

print('<14.>')
print('4번 SyntaxError')   ##########

print('\n====================\n')

print('<15.>')
print('4번')

print('\n====================\n')

print('<16.>')
print('숫자가 아닙니다.')

print('\n====================\n')

print('<17.>')
print('1) NameError\n2) IOError\n3) RuntimeError\n4) KeyError' )

print('\n====================\n')

print('<18.>')
print('Not divided by 0')

print('\n====================\n')

print('<19.>')
print("with open('i_have_a_dream.txt', 'r') as f:\n\tcontents = f.read()\n\tprint(contents)")