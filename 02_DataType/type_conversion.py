"""
# 타입 변환
# str() 함수 : 숫자를 문자열로 변환
# print('나는 현재 나이가 ' + str(23) + "살입니다")
'''
# int() : 정수형식의 문자열을 정수로 변환
num = input('숫자를 입력하세요 : ')   # 키보드로 입력받은 자료를 num 변수에 할당
# print(type(num))
print(num + 100)
'''
'''
print(int('123', 8))   # 8진수 : 0o123, 2진수 : 1010011
print(int('123', 16))
print(int('1111', 2))
'''

# float(문자열) : 문자열을 실수로 변환
print(float(num) + 100)
"""

# 키보드부터 두 개의 정수를 입력받고,
# 두 수의 합과 평균을 구한 후 합과 평균을 출력하시오.

num1 = int(input('첫 번째 정수를 입력하세요 : '))
num2 = int(input('두 번째 정수를 입력하세요 : '))

sum = num1 + num2
average = sum / 2

print('합은 ' + str(sum) + ',', '평균은 ' + str(average))
print('합은 {}, 평균은 {}'.format(sum, average)) # 이게 제일 편한 것 같다!
print('합은 {0}, 평균은 {1}'.format(sum, average))
print('합은 %d, 평균은 %.1f' % (sum, average))

print(format(sum, '10.2f'))

print('합은 {0:d}, 평균은 {1:9.2f}'.format(sum, average))
print('평균은 {1:9.2f}, 합은 {0:d}'.format(sum, average))
