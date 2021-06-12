# 파일 생성 : 파일명만 적기
# f = open("file1.txt", 'w')
# f.close()
# 생성된 file1.txt 파일은 빈 파일

# 경로 수정 : 디렉토리가 존재하지 않는 경우
# f = open("d:/PythonStudㅇ/file1.txt", 'w')
# f.close()
# FileNotFoundError: [Errno 2] No such file or directory: 'd:/PythonStudㅇ/file1.txt'

# 디렉토리 경로 설정 시 \ 사용하면 오류 발생   =>   \\ 또는 /로 수정!
# 파일의 절대경로
# f = open("d:\PythonStudy\file2.txt", 'w')
f = open("d:\\PythonStudy\\file2.txt", 'w')
f.close()
# OSError: [Errno 22] Invalid argument: 'd:\\PythonStudy\x0cile1.txt'

# 상대경로 표현
f = open("../file.txt", 'w')   # 하나 상위 폴더에 만들기
f.close()
# D:/PythonStudy/file.txt   ->   PythonStudy에 file.txt로 저장