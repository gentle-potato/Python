print('#2 점수 리스트')

scoreL = []
total = 0
cnt = 0

n = int(input('학생 수 입력 : '))
for i in range(1, n+1) :
    score = int(input('학생%d 점수 입력 : ' % i))
    scoreL.append(score)
    if score >= 80 :
        cnt += 1
    total += score
print(cnt)
print('총점 : %d' % total)
print('평균 : %.2f' % float(total/n))
print('80점 이상 학생 : %d명' % cnt)

print('\n=============================\n')

print('#5 사자성어 맞추기')

print('구글 드라이브에서 유화영씨꺼 코드 보기 -> while True 사용(단, randint가 반복문 안으로 들어가야 함)')