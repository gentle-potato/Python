# 리스트의 요소를 정렬 : sort(), reverse() / sorted() 함수
a = [3, 6, 0, -4 ,1]
print(a)
# a.sort()   # 오름차순 정렬
# a.sort(reverse = True)   # 내림차순 정렬
# a.reverse()   # 역순 정렬
# print(a)

# reverse() 메소드를 사용하지 않고 리스트를 역순으로 생성하여 출력하기
b = []
for i in range(len(a)) :
    # item = a.pop()
    # print(item)
    # b.append(item)
    b.append(a.pop())
print(a)
print(b)

# sorted() 함수
a = [3, 6, 0, -4 ,1]
c = sorted(a)   # 정렬된 a 리스트를 c에 할당
print(a)
print(c)

string = ['GRAPE', 'Apple', 'aPPle', 'banana', 'melon', 'apple']
string.sort()
print(string)
string.sort(key = str.lower)   # 대소문자 구분 X
print(string)
string.sort(key = str.upper)   # 대소문자 구분 X
print(string)

# max(), min() 함수
a = [3, 6, 0, -4 ,1]

print(max(a))
print(min(a))

print(max(string))
print(min(string))