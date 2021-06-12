# # 파일에 쓰기 w : write()

# # 여러 줄의 데이터 쓰기
# f = open('file3.txt', 'w', encoding='utf-8')
# for i in range(1, 11) :
#     data = '%d행' % i
#     f.write(data)
# f.close()
# 파일 내용 : 1행2행3행4행5행6행7행8행9행10행

# # 탭으로 구분하여 출력
# f = open('file4.txt', 'w', encoding='utf-8')
# for i in range(1, 11) :
#     data = '%d행\t' % i
#     f.write(data)
# f.close()
# 파일 내용 : 1행	2행	3행	4행	5행	6행	7행	8행	9행	10행

# # 한 줄 단위로 출력
# f = open('file4.txt', 'w', encoding='utf-8')
# for i in range(1, 11) :
#     data = '%d행\n' % i
#     f.write(data)
# f.close()

# # ',' 넣어서 csv 파일 형식으로 저장
# f = open('file4.csv', 'w', encoding='utf-8')
# for i in range(1, 11) :
#     data = '%d행,' % i
#     f.write(data)
# f.close()

f = open('file4.csv', 'w', encoding='utf-8')
for i in range(1, 11) :
    if i == 10 :
        data = '%d행' % i
    else :
        data = '%d행,' % i
    f.write(data)
f.close()