# for문의 이해

for name in ['홍길동', '이몽룡', '성춘향', '변학도'] :   # 리스트의 길이 만큼 반복
    print(name)
for num in range(0, 10) :   # 10보다 하나 작은 값, 즉 9까지!
    # print(num)
    print(num, end = ' ')   # 한 줄에 프린트
print('\n==========================')
for num in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] :
    print(num, end = ' $ ')   # 한 줄에 프린트 + 사이사이에 $ 집어넣기