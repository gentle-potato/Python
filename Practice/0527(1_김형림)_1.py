print('===== 1. Yesterday 가사 ======')

# Yesterday 가사를 모두 소문자로 변경하여 data에 할당
f = open('yesterday.txt', 'r', encoding='utf-8')
data = f.read()
data = data.lower()
f.close()

# 소문자로 변경된 가사를 새롭게 yesterday.txt 파일에 새로 작성
f = open('yesterday.txt', 'w', encoding='utf-8')
f.write(data)
f.close()

# 가사를 공백을 기준으로 분할 / 리스트로 정리된 값을 오름차순으로 정렬
f = open('yesterday.txt', 'r', encoding='utf-8')
data = f.read()
data = data.split()
data.sort()
# print(data)
f.close()

# 딕셔너리를 만들고, 그 안에 단어마다의 개수를 정리
dict = {}

for i in range(len(data)) :
    dict[data[i]] = 0

for i in range(len(data)) :
    dict[data[i]] += 1

# 만들어진 딕셔너리를 세로로 출력
for i in range(len(dict)) :
    print(f"'{list(dict.keys())[i]}': {list(dict.values())[i]}")