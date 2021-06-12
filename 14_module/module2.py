# calculaor module 참조
import calculator
from calculator import div, add, mul
from calculator import *

a = calculator.add(9, 8)
print(a)
print(calculator.mul(10, 5))
print(add(5, 2))
print(div(3, 5))

import showInfo   # 모듈의 모든 함수 참조
from showInfo import *   # all   ->   import showInfo와의 차이점은 모듈의 이름(showInfo)을 입력하지 않아도 된다는 것

showInfo.show_name()
show_name()
print('module2.py __name__ :', __name__)