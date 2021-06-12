# formatting : %d, %f, %s, %c
# %3d, #5.2f

alphas = 20 ; digits = 30
height = 179.33
string = 'Python'
print('문자 : %d개' % alphas)
print('문자 : ', format(alphas, 'd'), '개')
print('문자 : {0}개, 숫자 : {1}개'.format(alphas, digits))
print('문자 : {alp}개, 숫자 : {dig}개'.format(alp = alphas, dig = digits))
print('키는 {0:5.1f}'.format(height))
print('{0:<10}'.format(string))   # 왼쪽 정렬
print('{0:>10}'.format(string))   # 오른쪽 정렬
print('{0:^10}'.format(string))   # 가운데 정렬
print('{0:-^10}'.format(string))   # 가운데 정렬하고 나머지 -로 채우기
print(string.ljust(10))   # 문자열의 왼쪽, 오른쪽, 가운데 정렬
print(string.rjust(10))
print(string.center(10))

# 날짜, 시간 출력 포맷
from datetime import date, datetime, timedelta

today = date.today()
print(today.year)
print(today.month)
print(today.day)

cur_time = datetime.now().time()   # 시분초 제외
print(cur_time)
print(cur_time.hour)
print(cur_time.minute)
print(cur_time.second)
print(cur_time.microsecond)

cur_time = datetime.now()   # 시분초 제외
print(today + timedelta(days = -1))   # timedelta : 날짜 계산
print(today + timedelta(days = 7))
print(cur_time + timedelta(days = 1, hours = 2))

print(today.strftime('%Y-%m-%d %H:%M:%S'))   # ftime : format time