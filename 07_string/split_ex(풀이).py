birthday = input('생일 입력(연/월/일) : ')
birth_split = birthday.split('/')
print('당신은 %s년에 태어나셨군요.' % birth_split[0])
print('생일은 %s월 %s일이네요.' % (birth_split[1], birth_split[2]))

print('\n======================\n')

print('# 심화해서 데이터의 형태가 일정하지 않을 때를 가정')
data = "{a1:30 }, {a 2:50}, {a3: 20}, {a4 :70}, {a5:40}"

split_data = data.split(',')
score = n = total = 0   # n은 학생 수

for d in split_data :
    item1 = d.split(':')   # d = {a1:30}   =>   ['{a1', '30}']
    item2 = item1[1].split('}')   # '30}'   =>   ['30']
    score = int(item2[0])
    # 또는 item2를 없애고 score = int(item1[1].split('}')[0])로 한 번에!
    print(score)
    total += score
    n += 1

print(f'총점은 {total}, 평균은 {total/n}')