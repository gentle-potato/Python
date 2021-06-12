# 문자열의 구성요소 판단
# isalpha() : 문자 여부 True/False
# isdigit() : 숫자
# isspace() : 공백
# isalnum() : 영어 혹은 숫자인지
# islower() : 소문자
# isupper() : 대문자

text = '1234567num'
print(text.isalpha())
print(text.isdigit())
print('   '.isspace())
print(text.isalnum())
print('Abc'.islower())
print('AAA'.isupper())

print('1'.isalpha())
print('a'.isdigit())
print('A'.islower())
print('A'.isupper())

# 연습문제 : 문장을 입력하여 문자와 숫자, 스페이스, 그 외 문자의 개수를 출력
# '나의 email 주소는 imlkm70@daum.net 입니다'
alphas = digits = space = others = 0
string = input('문장을 입력하세요 : ')

for c in string :
    if c.isalpha() :
        alphas += 1
    elif c.isdigit() :
        digits += 1
    elif c.isspace() :
        space += 1
    else :
        others += 1

print('문자 : %d개' % alphas)
print('숫자 : %d개' % digits)
print('공백 : %d개' % space)
print('그 외 : %d개' % others)