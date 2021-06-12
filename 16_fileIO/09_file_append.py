# append mode를 사용하여 파일 끝에 추가
# f = open('test2.txt', 'a', encoding='utf-8')
# data = '\n\nPython programming'
# f.write(data)
# f.close()

# 읽기모드로 파일을 열어서 내용 출력
f = open('test2.txt', 'a', encoding='utf-8')
data = '\nR programming\n'
f.write(data)
f.close()

f = open('test2.txt', 'r', encoding='utf-8')
print(f.read())
f.close()