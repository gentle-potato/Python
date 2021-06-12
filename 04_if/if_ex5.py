# 도형을 선택해서 면적 구하기

"""
도형 입력(1 : 사각형, 2 : 삼각형, 3 : 원) : 1
가로 입력 : 10
세로 입력 : 20
사각형의 면적 = 200

도형 입력(1 : 사각형, 2 : 삼각형, 3 : 원) : 2
밑변 입력 : 10
높이 입력 : 20
삼각형의 면적 = 100

도형 입력(1 : 사각형, 2 : 삼각형, 3 : 원) : 3
반지름 입력 : 10
원의 면적 = 314.16
"""

shape = float(input('도형을 입력하세요(1 : 사각형, 2 : 삼각형, 3 : 원) : '))

if shape == 1 :
    length_1 = float(input('가로 입력 : '))
    height_1 = float(input('세로 입력 : '))
    area_1 = length_1 * height_1
    print('사각형의 면적 = %f' % area_1)
elif shape == 2 :
    length_2 = float(input('밑변 입력 : '))
    height_2 = float(input('높이 입력 : '))
    area_2 = length_2 * height_2 / 2
    print('삼각형의 면적 = %f' % area_2)
elif shape == 3 :
    r = float(input('반지름 입력 : '))
    area_3 = r ** 2 * 3.141592
    print('원의 면적 = %f' % area_3)
else :
    print('1, 2, 3 중에서 입력하세요!')