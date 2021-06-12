# 집합적 자료형 : tuple
# 삭제, 변경, 추가 작업 불가

# 리스트 생성 : list() or []
# tuple 생성 : tuple() or ()
t1 = tuple()
t2 = ()

t1 = (1, 2, 3)
print(t1)
print(type(t1))

t2 = 1, 3, 4
print(t2)

t3 = t1, (5, 6, 7)
print(t3)

t4 = [1, 4], [5, 6]
print(t4)

t5 = tuple([1, 4])   # list -> tuple
print(t5)

# 튜플의 요소 다루기
# 요소 변경 불가
print(t1[2])
# t1[2] = 10

# 요소 추가 및 삭제 불가
# t1.append(-9)
# del(t1[2])

list1 = [1, 2, 3]
del(list1[1])
print(list1)

# del(t1)   # 튜플 자체를 지우는 건 가능

print('\n------------------\n')

# tuple.index(), .count()
tt = 'a', 'b', 'c', 'e', 'a', 'd'
i = tt.index('e')
print(i)
c= tt.count('a')
print(c)

# slicing
t = tt[:]
t = tt[1:5]
print(t)

# +, * 연산
print(t1 + t2)
print(tt*2)

# tuple 연습문제
print('# tuple 연습문제')
tt = ((1, 2, 3), (4, 5 ,6), (7, 8, 9))
print(tt[1][2])

for x in tt :
    for y in x :
        print(y, end = ' ')
    print()

print('# 또는')
for a in tt :
    print(a[0], a[1], a[2])

# tuple
myTuple = (10, 20, 30)
myList = list(myTuple)
print(type(myList))
print(myList)
myList.append(40)
print(myList)
myTuple = tuple(myList)
print(myTuple)   # myTuple = (10, 20, 30, 40)

print(t4[0])
print(type(t4[0]))
t4[0][0] = 10
print(t4)

# list 객체의 메소드들
# dir(list())
# ['__add__', '__class__', '__class_getitem__', '__contains__',
#  '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__',
#  '__format__', '__ge__', '__getattribute__', '__getitem__',
#  '__gt__', '__hash__', '__iadd__', '__imul__', '__init__',
#  '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__',
#  '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
#  '__repr__', '__reversed__', '__rmul__', '__setattr__',
#  '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
#  'append', 'clear', 'copy', 'count', 'extend', 'index',
#  'insert', 'pop', 'remove', 'reverse', 'sort']

# tuple 객체의 메소드들
# dir(tuple()
# ['__add__', '__class__', '__class_getitem__', '__contains__',
#  '__delattr__', '__dir__', '__doc__', '__eq__', '__format__',
#  '__ge__', '__getattribute__', '__getitem__', '__getnewargs__',
#  '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__',
#  '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__',
#  '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__',
#  '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']