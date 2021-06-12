# readline() 함수를 이용하여 파일 읽어오기

# readline() : 1개의 행씩 읽어오기, 행 끝에 '\n' 포함
# redadlines() : 모든 행을 읽어 라인 단위별로 잘라서 리스트를 생성
#                ['...\n', '...\n', '...\n', ...,  '...\n']
# read() : 내용 전체를 한 문자열로 반환 ''' '''

print('-----첫 번째 행 읽어오기-----')
# # ANSI 형식으로 저장된 파일 열기
# f = open('test.txt', 'r')
# line = f.readline()
# print(line)
# f.close()

# # UTF-8로 저장된 파일 읽어오기
# f = open('test.txt', 'r')
# line = f.readline()
# print(line)
# f.close()
# # 오류 발생
# # UnicodeDecodeError: 'cp949' codec can't decode byte 0xec in position 0: illegal multibyte sequence

# # 인코딩 UTF-8로 지정하여 해결
# f = open('test.txt', 'r', encoding='utf-8')
# line = f.readline()
# print(line)
# f.close()

# # 여러 줄 읽기
# print('-----여러 줄 읽기-----')
# f = open('test.txt', 'r', encoding='utf-8')
# line = f.readline()
# print(line)
# line = f.readline()
# print(line)
# f.close()
# # 출력 형식 :
# # 안녕하세요. 홍길동입니다.
# #
# # 지금 파이썬을 공부하는 중이에요.
# #

f = open('test.txt', 'r', encoding='utf-8')
line = f.readline()
print(line, end='')   # readline은 한 줄 띄어서 나오므로 붙여주려면 end='' 사용
line = f.readline()
print(line, end='')
f.close()

# 파일 전체 읽기
print('-----파일 전체 읽기-----')
f = open('test.txt', 'r', encoding='utf-8')
while True :
    line = f.readline()
    if line == '' :
        break
    print(line, end='')
f.close()

print('\n# 또는')
f = open('test.txt', 'r', encoding='utf-8')
while 1 :
    try :
        line = f.readline()
        line != ''
        print(line, end='')
    except Exception :
        break
f.close()
# 이 경우 프린트는 되지만, 실행이 종료되지 않는다! 이유가 뭐지...