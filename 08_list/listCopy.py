# 리스트의 복사


# 얕은 복사(shallow copy)
scores = [65, 70, 90, 89, 78]
value = scores

print('scores :', scores)
print('value :', value)

scores[3] = 98
print('scores 값 변경 :', scores)
print('value :', value)   # scores를 변경했더니 value도 변경된다!

value[0] = 100
print('scores 값 변경 :', scores)
print('value :', value)   # value를 변경했더니 scores도 변경된다!


# 해결 방법은 깊은 복사(deep copy) : .copy(), list(), deepcopy()
value2 = scores.copy()
print('value2 :', value2)
scores[0] = 50
print('scores :', scores)
print('value :', value)
print('value2 :', value2)

# 또는
value3 = list(scores)   # list()를 사용해서 복사
print('value3 :', value3)
print('scores :', scores)
scores[0] = 150
print('scores :', scores)
print('value3 :', value3)

# 또는 deepcopy라는 모듈 사용
import copy
value4 = copy.deepcopy(scores)
scores[2] = 300
print('scores :', scores)
print('value3 :', value3)