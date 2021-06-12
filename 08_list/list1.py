# 리스트의 기본 개념

intL = [1, 3, 2, 10]
floatL = [1.5, 3.2, 5.4]
nameL = ['홍길동', '이몽룡', '성춘향', '변학도']
numL = [1, 3, 4, [1, 2]]   # 리스트 안에 리스트도 들어갈 수 있음
samL = [1, 3, .5, '하하']   # 리스트는 다양한 형식을 포함할 수 있음

print(intL)
print(type(intL))
print(numL)
print(samL)

for x in numL :
    print(x)

for i in range(len(numL)) :
    print(numL[i])

a, b, c = floatL   # a, b, c에 각각 하나씩 할당
print(a)
print(b)
print(c)



# split_ex 또 다른 풀이
data = "{a1:30 }, {a 2:50}, {a3: 20}, {a4 :70}, {a5:40}"

split_data = data.split(',')
n = total = 0   # n은 학생 수

for d in split_data :
    id, score = d.split(':')   # d = {a1:30}   =>   ['{a1', '30}']
    print(id, ',', score)
    score = int(score.split('}')[0])   # '30}'   =>   ['30']   =>   30
    # item2 = item1[1].split('}')   # '30}'   =>   ['30']
    # score = int(item2[0])
    # # 또는 item2를 없애고 score = int(item1[1].split('}')[0])로 한 번에!
    print(score)
    total += score
    n += 1

print(f'총점은 {total}, 평균은 {total/n}')

# 인덱싱(indexing) & 슬라이싱(slicing)
print(nameL[-1])
print(nameL[:])
print(nameL[1:3])
print(numL[-1][0])   # 리스트 안에 리스트가 있는 경우

# allL = []   # 빈 리스트 생성
# allL = list()   # 마찬가지
# print(allL)

allL = [intL, floatL, nameL, numL]
print(allL)
print(allL[-1][-1][0])   # 리스트 안에 리스트 안에 리스트가 있는 경우

print(nameL[:-1])
print(nameL[-1:])   # 리스트의 형태로 가져옴
print(nameL[-1])   # 요소만 가져옴
n = len(nameL)
print(nameL[:n])

# 리스트의 +, * 연산
sumL = numL + samL   # 리스트 합치기 가능
print(sumL)
print(numL * 3)   # 리스트 반복 가능

# 리스트의 내용 변경
print(numL)
numL[-1] = 10
print(numL)
numL[2:4] = []   # 삭제
print(numL)