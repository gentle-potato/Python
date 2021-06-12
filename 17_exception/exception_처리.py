# 예외 발생 상황 처리

# ZeroDivisionError: division by zero
# print(10/0)
try :
    print(10/0)
    # print(10/2)
except :
    print('ZeroDivisionError')
finally :   # 오류 발생 여부와 관계 없이 항상 나오는 부분
    print('나누기')

# 예외처리 클래스 지정
try :
    print(10/0)
    # print(10/2)
except Exception :
    print('ZeroDivisionError')
finally :
    print('나누기')

try :
    print(10/0)
    # print(10/2)
except ZeroDivisionError :
    print('0으로 나누었네요...')
finally :
    print('나누기')

try :
    print(10/0)
    # print(10/2)
except ZeroDivisionError as e :
    print('0으로 나누었네요... : ', e)   # 에러에 대한 구체적인 설명 : 별칭 e 사용
finally :
    print('나누기')

# TypeError: can only concatenate str (not "int") to str
# print('age=' + 23)
try :
    print('age=' + 23)
except TypeError as e :
    print(e)

# 예외처리를 여러 개 지정하더라도 가장 먼저 나온 에러만 처리
try :
    print('age=' + 23)
    print(10 / 0)
except ZeroDivisionError as e:
    print('0으로 나누었네요... : ', e)   # 가장 먼저 발생한 오류에 대한 것만 반환
except TypeError as e :
    print(e)

# 여러 개의 예외처리 : 함께 처리 가능
try :
    print('age=' + 23)
    print(10 / 0)
except (ZeroDivisionError, TypeError) as e:
    print(e)

#
try :
    num = int(input('input number : '))
except ValueError :
    print('정수가 아닙니다.')
else :   # 에러가 아니면 실행
    print(num)
finally :
    print('종료')

try :
    f = open('testex.txt', 'r')
except FileNotFoundError :
    pass
else :
    data = f.read()
    print(data)
    f.close()
finally :
    print('종료')

# NameError: name 'x' is not defined
# print(x)

# ValueError: incomplete format
# a = 100
# print("%d%" % a)

# SyntaxError: invalid syntax
# if x>10
#     print('Kim')

# IndexError: list index out of range
# a = [1, 2, 3]
# print(a[3])

# unboundLocalError
# def add() :
#     a += 1

# ModuleNotFoundError: No module named 'modd'
# import modd

# FileNotFoundError: [Errno 2] No such file or directory: 'readfile.txt'
# f = open('readfile.txt', 'r')
# data = f.read()

# OSError: [Errno 22] Invalid argument: 'd:\readfile.txt'
# f = open('d:\readfile.txt', 'r')