# split() 연습문제

#1
birth = input('생일 입력(연/월/일) : ')
birthL = birth.split('/')
print(birthL)
print(f'당신은 {birthL[0]}년에 태어나셨군요.\n생일은 {birthL[1]}월 {birthL[2]}일이네요.')
# 생일 입력(연/월/일) : 1998/09/20
# 당신은 1998년에 태어나셨군요.
# 생일은 9월 20일이네요.

print('\n======================\n')

# 2 주어진 데이터에서 점수만 추출하여 숫자화하고, 총점과 평균을 구하시오.
data = "{a1:30},{a2:50},{a3:20},{a4:70},{a5:40}"
dataP = data.split(',')
print(dataP)

students = len(dataP);
total = 0

for i in range(students) :
    score = dataP[i][4:6]
    total += int(score)

print(f'총점은 {total}, 평균은 {total / students}')

# split을 이용하여 분리
# 문자열.split(':')

# 첫 번째 분리된 결과는 리스트 형태로 주어지므로 반복문 for를 사용하여 다음 분리 때 활용
# 리스트의 요소를 가지고 오려면 [] 사용