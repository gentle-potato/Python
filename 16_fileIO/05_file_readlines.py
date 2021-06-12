# readline() : 1개의 행씩 읽어오기, 행 끝에 '\n' 포함
# redadlines() : 모든 행을 읽어 라인 단위별로 잘라서 리스트를 생성
#                ['...\n', '...\n', '...\n', ...,  '...\n']
# read() : 내용 전체를 한 문자열로 반환 ''' '''

# ==============================================

# 파일 전체 읽기
f = open('test.txt', 'r', encoding='utf-8')
lines = f.readlines()
print(lines)
print(type(lines))   # \n이 뒤에 붙은 리스트 형태로 반환
f.close()

# 파일 전체를 읽고 각 행을 리스트에 저장하기
# readlines() 결과와 동일
print('\n-----파일 전체 읽기-----')
f = open('test.txt', 'r', encoding='utf-8')
myL = []
while True :
    line = f.readline()
    if line == '' :
        break
    myL.append(line)
    print(line, end='')
f.close()
print('\n')
print(myL)   # readlines() 결과와 동일

# readlines()로 읽은 내용을 한 줄씩 출력하기
print('\n# readlines()로 읽은 내용을 한 줄씩 출력하기')
f = open('test.txt', 'r', encoding='utf-8')
lines = f.readlines()
for i in range(len(lines)):
    print(lines[i], end='')
f.close()