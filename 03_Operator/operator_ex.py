# 현금이 5000원이 있고, 사탕 가격이 120원인 경우
# 최대한 살 수 있는 사탕의 개수와 나머지 돈은 얼마인가?

cash = 5000
candyP = 120

a = cash // candyP
b = cash % candyP

print('사탕의 개수 : {0}개, 나머지 돈 : {1}원'.format(a, b))
print('1. 사탕의 개수 : {0}개\n2. 나머지 돈 : {1}원'.format(a, b))
print('사탕의 개수는 %d개, 나머지 돈은 %d원입니다~' % (a, b))