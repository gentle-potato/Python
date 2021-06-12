print('#1번, #2번, #3번, #4번,')
def print_coin() :
    print('비트코인')

print_coin()

# print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin()
# print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin()
# print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin()
# print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin()
# print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin()
# print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin()
# print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin()
# print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin() ; print_coin()

def print_coins() :
    for i in range(100) :   # i가 쓰이지 않을 때는 _로 표시해도 됨!
        print_coin()

# print_coins()

print('\n=======================\n')

print('#5번')
print('함수를 정의하기 전에 호출했기 때문이다.')

print('\n=======================\n')

print('#6번')
print('----------예측----------')
print('A\nB\nC\nA\nB')
print('----------결과----------')
def message() :
    print("A")
    print("B")

message()
print("C")
message()

print('\n=======================\n')

print('#7번')
print('----------예측----------')
print('A\nA\nC\nB')
print('----------결과----------')
print("A")

def message() :
    print("B")

print("A")
print("C")
message()

print('\n=======================\n')

print('#8번')
print('----------예측----------')
print('A\nC\nB\nE\nD')
print('----------결과----------')
print("A")
def messages1() :
    print("B")

print("C")
def messages2() :
    print("D")

messages1()   # 함수가 정의되지 않아서 에러, s 추가
print("E")
messages2()   # 함수가 정의되지 않아서 에러, s 추가

print('\n=======================\n')

print('#9번')
print('----------예측----------')
print('B\nA')
print('----------결과----------')
def message1() :   # 콜론 빠져서 에러
    print("A")

def message2() :   # 콜론 빠져서 에러
    print("B")
    message1()

message2()
print('\n=======================\n')

print('#10번')
print('----------예측----------')
print('B\nC\nB\nC\nB\nC\nA')
print('----------결과----------')
def message1() :   # 콜론 빠져서 에러
    print("A")

def message2() :   # 콜론 빠져서 에러
    print("B")

def message3() :   # 콜론 빠져서 에러
    for i in range (3) :
        message2()
        print("C")
    message1()

message3()