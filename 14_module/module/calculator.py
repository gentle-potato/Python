# calculator module

# 계산기 함수 : add(x, y), sub(x, y), mul(x, y), div(x, y)
def add(x, y) :
    return x+y
def sub(x, y) :
    return x-y
def mul(x, y) :
    return x*y
def div(x, y) :
    return x/y

print('calculator.py __name__ :', __name__)

# __name__ 변수 사용 : '__main()__'   ===>   이 파일 안에서만 아래 문장이 실행되고, import 할 때는 실행 안 됨!
if __name__ == '__main__' :
    print('Here is Caㅣculator module')
    print('__name__ :', __name__)