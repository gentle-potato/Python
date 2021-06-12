# 현금이 5000원이 있고, 사탕 가격이 120원인 경우
# 최대한 살 수 있는 사탕의 개수와 나머지 돈은 얼마인가?

money = 5000
candyP = 120
num = money // candyP
res = money % candyP
print('사탕은 %d개이고 남은돈은 %d원' %(num, res))
