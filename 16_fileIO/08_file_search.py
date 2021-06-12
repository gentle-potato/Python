# read() 함수 이용하여 원하는 내용이 파일에 있는지 검색
value = input('겁색어 입력 : ')
f = open('test2.txt', 'r', encoding='utf-8')
data = f.read()
if value in data :
    print('%s은(는) 있다!' % value)
else :
    print('%s은(는) 없다...' % value)
f.close()