# 5/18 실습문제

#1 16진수 구분 코드
print('#1 16진수 구분 코드')
num = input('16진수 한 글자 입력 : ')

'''
if num == 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'a' or 'b' or 'c' or 'd' or 'e' or 'f' :
# in 말고 ==과 or를 사용하면 에러가 나는 이유?
    x = int(num, 16)
    print('10진수  ==>  %d\n' % x)
else :
    print('16진수가 아닙니다\n')
print(end = '=============================\n\n')
'''

print('# 다른 방법')
if ('0' <= num and num <= '9') or ('A' <= num and num <= 'F') or ('a' <= num and num <= 'f') :
# num의 자료형을 print 해보면 문자열이므로 ''를 붙여줘야 함!
    x = int(num, 16)
    print('10진수  ==>  %d\n' % x)
else :
    print('16진수가 아닙니다\n')
print(end = '=============================\n\n')

print('#2 현금 교환')
# 하나하나 변수를 만들 필요 X! 잔돈 변수는 하나로 사용해도 됨!