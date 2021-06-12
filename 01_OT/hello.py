'''
# 첫 번째 프로그램
print('Kim Hyung Lim')
'''




'''
# 변수에 값을 저장(할당 : assign)
x = 10 ; y = 20 ; z = 30

x = 10
y = 20
z = 30

print(x, y, z)
print(x)
print(y)
print(z)

# 여러 개의 변수에 여러 개의 값을 저장
x, y, z = 10, 20, 30

print(x, y, z)
print(x)
print(y)
print(z)

# 여러 개의 변수에 동일한 값을 할당
a=b=c=100

print(a, b, c)
'''




"""
# 두 변수의 값을 교환(swap)
a, b = 10, 20

print('a =', a)
print('b =', b)


print('[swap]')
'''
c = a
a = b
b = c
'''


a, b = b, a

print('a =', a)
print('b =', b)
"""




'''
# 변수를 삭제
x = 100

print(x)
print(id(x))
print(type(x))

del x

print(x)
'''




'''
# 문자열에 큰 따옴표 사용
name = "김형림"
age = 27

print(name, age)

address = '서울특별시 강남구'

print(name + "은 " + address + "에 삽니다")
print(name + '은 ' + address + '에 삽니다')

# TypeError : 같은 자료형끼리만 연산 가능!
# str() : 숫자형을 문자열로 형변환
print(name + '은 ' + str(age) + '살입니다')
print(name + '은', age, '살입니다')
'''




'''
# 사각형의 면적을 구하는 프로그램
width = 100
height = 50
area = width * height

print("사각형의 면적은", area)
'''




"""
name = '홍길동'
no = 2016001
year = 4
grade = 'A'
average = 93.5

'''
print('성명 :', name)
print('학번 :', no)
print('학년 :', year)
print('학점 :', grade)
print('평균 :', average)

print('성명 : ' + name)
print('학번 :', no)
print('학년 :', year)
print('학점 : ' + grade)
print('평균 :', average)
'''

'''
#포맷 코드 사용
print('성명 : %s' % name)
print('학번 : %d' % no)
print('학년 : %d' % year)
print('학점 : %s' % grade)
print('평균 : %10.2f' % average)

print('이름 : %s, 학년 : %d' % (name, year))


rate = 80
print('이름 : %s, 출석률 : %d%%' % (name, rate))
'''


#format() 함수 사용
print(format(average, '.2f'))
"""




'''
kor = 90
eng = 80
math = 80

total = kor + eng + math
average = total / 3

print('총점: %d, 평균: %.2f' % (total, average))
'''




'''
INT_Rate = 0.03

deposit = 10000
interest = deposit * INT_Rate
balance = deposit + interest

print(balance)
print(int(balance))
print(format(int(balance), ','))
'''




'''
# 정수 리터럴
a = 0b1010 #2진수
b = 300 
c = 0o123 #8진수
d = 0x12fc #16진수

print(a, b, c, d)
'''




'''
# 특수 리터럴
# None
address = None

print(address)
print(type(address))
print(id(address))
'''




'''
a = 1 + 2 + 3 + \
    4 + 5 + 6

b = (1 + 2 + 3 +
     4 + 5 + 6)

print(a, b)
'''




'''
# 줄 안 바꾸고 프린트
print('first', end = "@")
print('second')

'''
