# set
s1 = set()
print(type(s1))
s1 = {3, 5, 7, 1, 3, 4}
print(s1)

# s2 = {[10, 20, 40]}   # 리스트로는 집합을 만들 수 없음
s2 = {(10, 20, 40)}   # 튜플로는 가능
print(s2)

# 인덱스 사용 불가
# s1[0]

# 데이터 추가 : .add()
s2.add(90)
print(s2)

s1.add(-9)
print(s1)

# 데이터 삭제 : remove()
s1.remove(-9)
print(s1)
# s1.remove(8)   # 삭제할 값이 없으면 에러
print(s1)

s1.discard(4)
print(s1)
s1.discard(0)   # 삭제할 값이 없으면 그냥 넘어감
print(s1)
s1.discard(7)
print(s1)

s1.clear()
print(s1)

del s1

# 집합 연산 : union, intersection, difference
s1 = {3, 4, 1, 6}
s2 = {2, 4, 5, 8, 3}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))   # 어느 것을 기점으로 하는냐에 따라 다르게 반환
print(s2.difference(s1))

print(s1 | s2)   # 합집합
print(s1 & s2)   # 교집합
print(s1 - s2)   # 차집합

# set 컴프리헨션
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)