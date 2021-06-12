# string 관련 함수들

# len() : 문자열의 length
string = 'Python Programming'
n = len(string)
print(n)

# count() : 문자열에서 찾고자하는 문자(열)의 개수
print(string.count('ing'))

# find() : 특정 문자(열)의 존재 여부에 따라 시작 위치 인덱스나 -1 반환
print(string.find('ing'))
print(string.find('ong'))   # 결과 : -1 -> 없음을 의미

# index() :
print(string.index('ing'))
print(string.index('ong'))   # 없는 경우 에러 발생