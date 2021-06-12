# 함수의 반환값(return)
def sum() :
    a = int(input('숫자1 입력 : '))
    b = int(input('숫자2 입력 : '))
    # print(a+b)
    return a + b   # 괄호 안 써도 됨

# res = sum()   # return을 해줘야 print 할 때 결과값을 반환! 안 하면 None 반환
# print('합은 %d' % res)
print('합은 %d' % sum())

#삼각형의 넓이 계산 함수 get_triangle_area()
# 높이와 밑변을 키보드로 입력
# 결과값을 반환
# 높이 :
# 밑변 :
# 삼각형의 면적 :

def get_triangle_area() :
    w = float(input('밑변 : '))
    h = float(input('높이 : '))
    area = 0.5 * w * h
    return area

area = get_triangle_area()
print('삼각형의 면적 : %.1f' % area)

# 반환값이 여러 개인 경우
# 반환값의 형식은 튜플
def get_triangle_area() :
    w = float(input('밑변 : '))
    h = float(input('높이 : '))
    area = 0.5 * w * h
    return w, h, area

area = get_triangle_area()
print('밑변 %d, 높이 %d, 삼각형의 넓이 %.2f' % (area[0], area[1], area[2]))   # return이 여러 개인 경우, 결과값은 튜플로 반환

def multiReturn() :
    return 1
    return 2
    return 3

print(multiReturn())   # return은 함수를 끝내면서 호출한 위치로 돌아가기 때문에 뒤의 return은 의미 없음

# 연습문제
def order() :
    p = int(input('상품가격 입력 : '))
    q = int(input('주문수량 입력 : '))
    print('------------------')
    t = p * q
    return p, q, t

z = order()
print(f'상품가격 : {z[0]:,}원\n주문수량 : {z[1]:,}개\n주문액 : {z[2]:,}원')

# 리스트 반환값
def getNames() :
    names = []
    for i in range(3) :
        name = input('이름 입력 : ')
        names.append(name)
    return names

nameL = getNames()
print(type(nameL))
print(nameL)

# 이름과 나이를 입력받아서 딕셔너리 형식으로 변환
# {'name': '홍길동', 'age': 20}
def name_age_dict() :
    dict = {}
    n = input('이름 입력 : ')
    g = input('나이 입력 : ')
    # dict['name'] = n ; dict['age'] = g
    dict = {'name': n, 'age': g}
    return dict

dict = name_age_dict()
print(dict)
print(type(dict))

print(dict[list(dict.keys())[0]])

for key, value in dict.items() :
    print(key, ':', value)

for key in dict.keys() :
    print(key, ':', dict[key])

# 반환값이 없는 경우 None 출력
def showHello() :
    print('Hello')

result = showHello()
print(result)