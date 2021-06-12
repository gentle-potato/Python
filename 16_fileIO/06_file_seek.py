# 파일 내에서 검색
# seek(offsetm whence) 함수

# 한글 utf-8 : 3바이트씩, utf-16: 2바이트씩
print('-----파일 내에서 검색 : seek()-----')
f = open('test2_utf-16.txt', 'r', encoding='utf-16')   # UTF-16으로 파일을 저장한 경우
f = open('test2.txt', 'r', encoding='utf-8')
# f.seek(0, 0)   # 시작 위치는 0행, 0열
# f.seek(1, 0)   # 시작 위치는 0행, 1열
# f.seek(7, 0)   # 시작 위치는 0행, 7열   =>   1행, 0열과 같음
# f.seek(15, 0)   # 오류 발생   =>   3바이트인 '가'가 쪼개지기 때문에
f.seek(14, 0)
# 한글은 3바이트   # UTF-8은 3byte, UTF-16은 2byte
lines = f.readlines()
print(lines)
f.close()