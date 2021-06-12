# 딕셔너리 dictionary
# 키와 값으로 구성 {키1:값1, 키2:값2, ...}

# 딕셔너리 만들기
d = {} ; d = dict()
d = {1: 'a', 2: 'b', 3: 'c'}   # item
print(d)
print(type(d))

# 딕셔너리 요소 접근
print(d[1])   # 딕셔너리는 인덱스가 아닌 키값으로 출력

d2 = {'name': 'Lee', 'tel': '010-1111-1111'}
print(d2['name'])

# 딕셔너리에 요소 추가
d[4] = 'f'
print(d)

d2['address'] = '서울시 강남구'
print(d2)

d3 = {'name': 'daum',
      'url': 'www.daum.net',
      'userid': 'dm',
      'pw': 1234}
print(d3)

# keys(), values(), items()
d3_Key = d3.keys()
print(type(d3_Key))
print(d3_Key)
print(list(d3_Key)[1])   # 리스트로 바꾸어서 출력해야 함

d3_Value = d3.values()
print(list(d3_Value))

d3_Item = d3.items()
print(d3_Item)   # item은 [(키, 값), ...]과 같이 튜블을 요소로 가진 리스트로 반환
print(list(d3_Item)[0])

for key in d3.keys() :   # 키를 통해 반복문 실행
    print(key)

for value in d3.values() :
    print(value)

for item in d3.items() :
    print(item)

print(d3['name'])
# print(d3['add'])   # 해당하는 게 없으면 에러가 남
print(d3.get('url'))
print(d3.get('add', 'not exist'))   # 해당하는 게 없으면 None이나 지정한 값(not exist) 반환

k = 'link'

if d3.get(k) is None :
    print(k + '에 대한 데이터가 없음')

# in / not in
print('link' in d3)
print('link' not in d3)

print('name' in d3)
print(dir(d3))
# ['__class__', '__class_getitem__', '__contains__', '__delattr__',
#  '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
#  '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__',
#  '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__',
#  '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__',
#  '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__',
#  '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get',
#  'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

print(d3.popitem())   # 가장 끝에 있는 아이템 가져옴
print(d3)

# zip()
# comprehension
y = [x**2 for x in (2, 3, 4)]
print(y)
z = {x: x**2 for x in (2, 3, 4)}
print(z)

for key, val in d3.items() :
    print('%s : %s' % (key, val))

students = {1: [80, 86, 60],
            2: [87, 90, 30],
            3: []}

endDict = {}
endDict['dog'] = '개'
endDict['cat'] = '고양이'
print(endDict)