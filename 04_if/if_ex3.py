# 정수 3개를 입력받아서 제일 큰 수를 출력

a = int(input('첫 번째 정수를 입력하세요 : '))
b = int(input('두 번째 정수를 입력하세요 : '))
c = int(input('세 번째 정수를 입력하세요 : '))

if a > b and a > c :
    max_num = a
elif a < b and b > c :
    max_num = b
else :
    max_num = c
print('제일 큰 수 : %d' % max_num)

# 더 간단하게 작성하면
if a > b and a > c :   # a > b, a < c
    max_num = a
elif b > c :
    max_num = b
else :
    max_num = c
print('제일 큰 수 : %d' % max_num)