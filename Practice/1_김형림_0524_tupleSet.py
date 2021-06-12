# 실습문제 : Tuple & Set
# 아래 내용을 파이참에 붙여넣기 하셔서 문제를 푸시고 #“회차_이름_0524_tupleSet.py”라는 실행파일과 #“회차_이름_0524_tupleSet.png”라는 결과물 캡처 파일을 구글드라이브에 #올려주세요.

# 1. my_variable 이름의 비어있는 튜플을 만들라.
my_variable = {}
print('#1 my_variable = {}')

print('\n=======================\n')

# 2. 다음 코드를 실행해보고 오류가 발생하는 원인을 설명하라.
# >> t = (1, 2, 3)
# >> t[0] = 'a'
# Traceback (most recent call last):
#  File "<pyshell#46>", line 1, in <module>
#  t[0] = 'a'
# TypeError: 'tuple' object does not support item assignment
print('#2 튜플은 수정 및 삭제가 불가능하기 때문에 오류가 발생한 것이다.')

print('\n=======================\n')

# 3. 숫자 1 이 저장된 튜플을 생성하라.
tuple1 = (1)
print('#3 tuple = (1)')

print('\n=======================\n')

# 4. 아래와 같이 t에는 1, 2, 3, 4 데이터가 바인딩되어 있다. t가 바인딩하는 데이터 타입은 무엇인가?
# t = 1, 2, 3, 4
t = 1, 2, 3, 4
print(type(t)) ; print('#4 t가 바인딩하는 데이터 타입은 튜플이다.')

print('\n=======================\n')

# 5. 변수 t에는 아래와 같은 값이 저장되어 있다. 변수 t가 ('A', 'b', 'c') 튜플을 가리키도록 수정 하라.
#  t = ('a', 'b', 'c')
t = ('a', 'b', 'c')
tlist = list(t)
tlist[0] = 'A' ; tlist[1] = 'B'; tlist[2] = 'C'
t = tuple(tlist)
print('#5', end=' ') ; print(t)

print('\n=======================\n')

# 6. 다음 튜플을 리스트로 변환하라.
# interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest = list(interest)
print('#6', end=' ') ; print(interest)

print('\n=======================\n')

# 7. 다음 리스트를 튜플로 변경하라.
# interest = ['삼성전자', 'LG전자', 'SK Hynix']
interest = ['삼성전자', 'LG전자', 'SK Hynix']
interest = tuple(interest)
print('#7', end=' ') ; print(interest)

print('\n=======================\n')

# 8. 파티에 참석한 사람이 다음과 같을 때 집합을 생성하고, 아래 조건에 맞게 출력하시오.
# partyA : "Park","Kim","Lee"
# partyB : "Park","길동","몽룡"
partyA = {"Park","Kim","Lee"}
partyB = {"Park","길동","몽룡"}

# 1) 파티에 참석한 모든 사람은?
print('#8')
print('1) 파티에 참석한 모든 사람은?', end=' ') ; print(partyA | partyB)
# 2) 2개의 파티에 모두 참석한 사람은?
print('2) 파티에 모두 참석한 사람은?', end=' ') ; print(partyA & partyB)
# 3) 파티 A에만 참석한 사람
print('3) 파티 A에만 참석한 사람', end=' ') ; print(partyA - partyB)
# 4) 파티 B에만 참석한 사람
print('4) 파티 B에만 참석한 사람', end=' ') ; print(partyB - partyA)