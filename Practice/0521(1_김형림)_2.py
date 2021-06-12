print('#4 점수 리스트 정렬')

scores = []

students = int(input('학생 수 입력 : '))

score = total = over_80 = 0
for x in range(students) :
    score = int(input(f'학생{x+1} 점수 입력 : '))
    scores.append(score)
    total += score
print(f'총점 : {total}\n평균 : {total/students:.2f}')

for x in range(len(scores)) :
    if scores[x] >= 80 :
        over_80 += 1
    else :
        pass
print(f'80점 이상 학생 : {over_80}명')
scores.sort(reverse = True)
print('점수 내림차순 정렬 :', scores)

print('\n=============================\n')

print('#5 사자성어 맞추기')

phases = ['개과천선', '구사일생', '군계일학', '무용지물', '동고동락', '유비무환', '입신양명', '괄목상대', '막역지우', '고장난명']
meanings = ['잘못을 고치고 옳은 길에 들어서다.', '죽을 고비를 여러 번 겪으며 살아나다.', '평범한 사람 가운데 뛰어난 사람', '아무짝에나 쓸모 없는 것',
         '고통과 즐거움을 함께 한다.', '미리 준비해두면 근심 걱정이 없다.', '사회적으로 인정받고 출세하여 이름을 세상에 드날리다.',
         '다른 사람의 학식이나 업적이 크게 진보한 것을 말한다.', '생사를 같이 할 수 있는 친밀한 벗', '상대 없이 혼자서는 어떤 일을 이룰 수 없다.']

print('사자성어 맞추기 게임을 시작합니다. :-)')
print('--------------------------------')

from random import randint
A = randint(0, 9)

question = input('%s\n이 말의 사자성어는? : ' % meanings[A])

while (question not in phases) or (A != phases.index(question)) :   # 순서 바뀌면 안 됨!★
    print('\n틀렸습니다... 다시 도전!')
    # from random import randint   # 이 문장은 제일 처음에만 선언해주면 됨!★
    A = randint(0, 9)

    question = input('\n%s\n이 말의 사자성어는? : ' % meanings[A])

print('\n맞습니다... 게임을 종료합니다.')