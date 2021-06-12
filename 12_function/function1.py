# 함수의 개요

# 함수 정의
def printHello() :
    print('Hello')

def printName(name) :
    print(name)

def area_square(width, height) :
    area = width * height
    return area

# 함수 호출
printHello()

printName('Lee')

w = 10
h = 20
area = area_square(w, h)
print(area)

# 연습문제
def show_info() :
    print(f'{my_name}\n{my_age}\n{my_phone_number}')
    return 0   # 아무것도 안 넣으면 출력할 때 None 반환

my_name = 'Mr. Gentle' ; my_age = 27 ; my_phone_number = '010-2583-0627'
result = show_info()

show_info()
print(result)

# 함수 이름 sum()
# 숫자 2개를 키보드로 입력받아서 두 수의 합을 출력
def sum() :
    num1 = int(input('숫자1 입력 : '))
    num2 = int(input('숫자2 입력 : '))
    sum = num1 + num2
    print(sum)
    return sum

sum()