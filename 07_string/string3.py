crawling = 'Data crawling is fun'

print(crawling.find('i'))
print(crawling.rfind('i'))
print(crawling.find('i', 1, 9))   # 찾을 부분 지정! 결과값 -1은 찾는 값이 없음을 나타냄

print('------------------')

print(crawling.index('i'))
print(crawling.rindex('i'))
# print(crawling.index('i', 1, 9))   # index는 찾는 값이 없으면 에러!

print('\n-----------------\n')

# split() : 지정된 문자로 문자열을 분할, 결과는 리스트 형식
token = crawling.split()
print(token)

names = 'Lee,Kim,Choi,Kang'
print(names.split(','))   # 콤마 단위로 쪼개갰다!   # ['Lee', 'Kim', 'Choi', 'Kang']

nameL = names.split(',')

for n in nameL :
    print(n)

for i in range(len(nameL)) :
    print(nameL[i])

# 문자열의 요소 하나씩 출력
for c in crawling :
    print(c)