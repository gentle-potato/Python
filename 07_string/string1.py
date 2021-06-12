# 문자열의 기본 형식과 이해

crawling = 'Data crawling is fun'
parsing = 'Data parsing is also fun'

print(crawling)
print(parsing)

print(type(crawling))
print(type(parsing))

PI = 3.1415
r = 10
result = '반지름 ' + str(PI) + '인 원의 넓이는 ' + str(PI * r * r)
print(result)

print('hello' * 3)

string = 'genle'
print(string[2])
print(string[-4])   # 0부터 시작
print(string[0])   # slicing : 문자열의 일부분을 추출

print(crawling[1:6])
print(crawling[:-1])
print(crawling[-1:])   # 마지막 문자
print(crawling[:])   # 문자열 전체
print(crawling[0 : 10])