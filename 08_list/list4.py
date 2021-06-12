# 리스트의 일치 검사
list1 = [1, 2, 4]
list2 = [2, 1, 3]

# ==, !=, >, <
print(list1 == list2)
print(list1 != list2)
print(list1 > list2)

# 2차원 리스트
list3 = [[1, 2, 3, 0], [4, 5, 6, 1], [7, 8, 9, 6]]
list4 = [[1, 2, 3], [1, 2], [1, 3, 4, 5]]
print(list3)

for i in list3 :
    print(i)

for i in list4 :
    for j in i :
        print(j, end = ' ')
    print()   # 다음 줄에 프린트하기 위해서!

print(list3[1][1])
print(len(list3))
print(len(list3[0]))

# 2차원 리스트 연습문제
print('# 2차원 리스트 연습문제')
# 10명의 학생의 국어, 영어, 수학 점수가 2차원 리스트 형식으로 저장된 경우
# 각 학생별 세 과목의 총점과 평균 점수를 계산하여 과목점수와 함께 출력하는 코드 작성

# [90, 85, 70]
# [88, 72, 92]
# [100, 100, 90]
# [90, 60, 50]
# ...

# 출력
# [90, 85, 70], 245, 81.7
# [88, 72, 92], 252, 8403
# [100, 100, 90], 290, 96.7
# [90, 60, 50], 200, 66.7
# ...

students = [[90, 85, 70], [88, 72, 92], [100, 100, 90], [90, 60, 50]]

for i in students :
    total = 0
    for j in i :
        total += j
    average = total/len(i)
    print(f'{i} {total} {average:.2f}')
print()

# 또는
print('# 또는')
for i in range(len(students)) :
    sum = students[i][0] + students[i][1] + students[i][2]
    print(f'{students[i]} {sum} {sum/len(students[i]):.2f}')