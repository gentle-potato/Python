# 파일에 쓰기 : 파일을 쓰기모드(w)로 열고,
# 파일객체의 write() 함수를 이용하여 파일에 출력(기록)
# data = 'hello'
# f = open('file2.txt', 'w')   # 파일객체 f
# f.write(data)
# f.close()

# data = '안녕하세요'
# f = open('file2.txt', 'w')   # 파일객체 f
# f.write(data)
# f.close()
# # 한글이 깨져 보임

# 한글인코딩 UTF-8 지정
data = '안녕하세요'
f = open('file2.txt', 'w', encoding='utf-8')   # 파일객체 f
f.write(data)
f.close()
# UTF-8 형식으로 저장 : 한글이 깨지지 않음