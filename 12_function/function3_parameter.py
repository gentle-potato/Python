# 함수의 매개변수(parameter)
# 함수에 전달(입력)되는 값 -> 함수 정의할 때

# 인수(argument) : 함수에 실제로 전달되는 값
def showInfo(name, age) :
    print('이름은 %s이고 나이는 %d세입니다.' % (name, age))

showInfo('홍길동', 18)

def getArea(width, height) :
    return width * height * 0.5

w = int(input('밑변 : '))
h = int(input('높이 : '))
print(getArea(w, h))

# 사칙연산을 수행하는 함수들을 정의하여 호출
# add(x, y)
# sub(x, y)
# mul(x, y)
# div(x, y)

# 2개의 숫자를 키보드로 입력받고, 각 함수에 전달하여 계산 결과를 아래와 같이 출력하는 코드 완성
# 10 + 5 = 15
# 10 - 5 = 5
# 10 * 5 = 50
# 10 / 5 = 2.0

def add(x, y) :
    return x + y
def sub(x, y) :
    return x - y
def mul(x, y) :
    return x * y
def div(x, y) :
    return x / y

x = int(input('숫자1 입력 : '))
y = int(input('숫자2 입력 : '))

print(f'{x} + {y} = {add(x, y)}\n'
      f'{x} - {y} = {sub(x, y)}\n'
      f'{x} * {y} = {mul(x, y)}\n'
      f'{x} / {y} = {div(x, y)}')

# 주문액, 할인액, 지불액 연습문제
print('# 주문액, 할인액, 지불액 연습문제')

def order(p, q) :
    total = p * q
    if total >= 100000 :
        discount = 0.1
    elif total >= 50000 :
        discount = 0.05
    else :
        discount = 0
    after_discount = total * (1 - discount)
    return total, total * discount, after_discount

p = int(input('상품 가격 입력 : '))
q = int(input('주문 수량 입력 : '))
print('--------------------')
order = order(p, q)
print(f'주문액 : {order[0]:>10,}원\n'
      f'할인액 : {order[1]:>10,.0f}원\n'
      f'지불액 : {order[2]:>10,.0f}원\n')
# 또는
print('주문액 : %s원' % format(order[0], ',.0f').rjust(10))
print('할인액 : %s원' % format(order[1], ',.0f').rjust(10))
print('지불액 : %s원' % format(order[2], ',.0f').rjust(10))